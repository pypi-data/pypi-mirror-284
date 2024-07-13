import time
from multiprocessing import Event, Process, Queue
from queue import Empty
from warnings import warn

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from mplserialscope.blitting import BlitManager

class MPLAnimator:
    """Animates a signal o-scope style from Serial-style output, with matplotlib blitting.

    For example, if the serial output is formatted like:
    time, sync_signal_1, sync_signal_2, test_voltage
    0, 0, 0, 0
    0.1, 0, 0, 0.25
    0.2, 0, 0, 0.50
    0.3, 0, 0, 0.25
    0.4, 0, 0, 0
    ...

    """

    def __init__(
        self,
        n_samples,
        fs,
        signal_header_name="therm",
        signal_yvals=None,
        bool_header_names=None,
        text_header_names=None,
        q_downsample=15,
    ):
        """Initializes the animator object

        Parameters
        ----------
        n_samples : int
            The number of samples to display in the animation

        fs : int
            The sampling frequency of the data

        signal_header_name : str
            The name of the signal, used to parse the correct column from the serial output

        signal_yvals : tuple
            The maximal desired y-limits for the signal plot

        bool_header_names : list of str
            List of boolean header names to parse from the serial output.
            Will be displayed as colored dots appearing in real time on the plot.

        text_header_names : list of str
            List of text header names to parse from the serial output.
            Will be displayed as real-time text annotations on the plot.

        q_downsample : int
            The downsample factor for the animation queue, to reduce computational power required.

        """

        # IO vars
        self.signal_header_name = signal_header_name
        self.bool_header_names = (
            bool_header_names if bool_header_names is not None else []
        )
        self.text_header_names = (
            text_header_names if text_header_names is not None else []
        )

        # Animator vars
        self.nsamp = n_samples
        self.current_val = 0
        self.fs = fs
        self.data = np.zeros((n_samples,), dtype="float")
        self.data_head_idx = 0  # to trace out data like an o-scope

        # MP vars
        self.queue = Queue()
        self.animator_exit_event = Event()
        self.animate_process = MPLAnimator.get_main_process(
            self.queue,
            self.fs,
            self.animator_exit_event,
            self.bool_header_names,
            self.text_header_names,
            n_samples=n_samples,
            ylims=signal_yvals,
        )
        self.q_downsample_counter = 0
        
        self.q_downsample = int(q_downsample)
        if q_downsample < 1:
            raise ValueError("q_downsample must be an integer >= 1") 

    @staticmethod
    def get_main_process(
        data_queue, fs, exit_event, bool_val_names, text_val_names, **kwargs
    ):
        """Open a blitting animate process.

        Parameters
        ----------

        data_queue : Queue
            The queue to send data to the animate process

        exit_event : Event
            The event to signal the animate process to close.

        kwargs : dict
            The keyword arguments to pass to the animate process
        """
        animate_process = Process(
            target=animated_plot_process,
            args=(data_queue, fs, exit_event, bool_val_names, text_val_names),
            kwargs=kwargs,
        )
        return animate_process

    def extract_indices_from_header(self, header):
        """Extract the indices of the signal, bools, and text from the header string.

        Parameters
        ----------
        header : str
            The header string from the serial output

        For example: "time, sync_signal_1, sync_signal_2, test_voltage"

        """
        header_list = [s.strip(" \r\n\t") for s in header.split(",")]
        self.signal_idx = [
            i for i, val in enumerate(header_list) if val == self.signal_header_name
        ]
        if len(self.signal_idx) == 0:
            raise ValueError(f"No col in header found for signal {self.signal_header_name}")
        elif len(self.signal_idx) > 1:
            raise ValueError(f"Multiple cols in header found for signal {self.signal_header_name}")
        else:
            self.signal_idx = self.signal_idx[0]

        if self.bool_header_names is not None:
            self.bool_signal_idx = [
                i
                for name in self.bool_header_names
                for i, val in enumerate(header_list)
                if val == name
            ]
        else:
            self.bool_signal_idx = []

        if self.text_header_names is not None:
            self.text_signal_idx = [
                i
                for name in self.text_header_names
                for i, val in enumerate(header_list)
                if val == name
            ]
        else:
            self.text_signal_idx = []

        return

    def start(self):
        """Calls the animate process to start if it's not already running."""
        if not self.animate_process.is_alive():
            self.animate_process.start()
        return

    def update(self, line):
        """Extract the data from the line and send to the animate process."""

        # Extract data from correct index in line
        self.current_val = np.array(line.split(",")[self.signal_idx], dtype="float")

        # Update vector
        self.data[self.data_head_idx] = self.current_val

        # Extract bool vals, if any
        if len(self.bool_signal_idx) > 0:
            bool_vals = [int(line.split(",")[idx]) for idx in self.bool_signal_idx]
        else:
            bool_vals = []

        # Extract text vals, if any
        if len(self.text_signal_idx) > 0:
            text_vals = [line.split(",")[idx] for idx in self.text_signal_idx]
        else:
            text_vals = []

        # Delete the oldest data to make it o-scope-like
        self.data[(self.data_head_idx + int(self.nsamp / 10)) % self.nsamp] = np.nan
        self.data_head_idx += 1
        self.data_head_idx = self.data_head_idx % self.nsamp

        # Increment downsample counter
        self.q_downsample_counter += 1
        self.q_downsample_counter = self.q_downsample_counter % self.q_downsample

        # Decide if sending to animator
        if self.q_downsample_counter == 0 and not self.animator_exit_event.is_set():
            self.queue.put((self.data, bool_vals, text_vals))

        return

    def close(self):
        """Close the animator process and queue. Force the queue to close"""

        # Empty the queue to prevent weird gc bug when closing queue
        while not self.queue.empty():
            self.queue.get()
        
        # Shut everything down
        self.animator_exit_event.set()
        self.queue.close()  # this can throw weird issues when it get's gc'd, but it's harmless, see https://github.com/python/cpython/pull/31913
        self.queue.join_thread()
        self.animate_process.join()


def animated_plot_process(
    data_queue,
    fs,
    exit_event,
    bool_val_names,
    text_val_names,
    n_samples=100,
    ylims=(0, 1023),
):
    """Run a blitting animated plot of some data that comes in via a queue."""

    # Set the backend to Qt5Agg for real time display
    matplotlib.use("Qt5Agg")

    # Prep data vector
    data = np.zeros((n_samples,))
    # queue_size_readable = True

    # Get the current time, for displaying time elapsed on the plot
    tic = time.time()

    ### SET UP BLITTING ###

    # Make a new figure
    fig, ax = plt.subplots()

    # Add the line for the signal
    xvals = np.arange(n_samples) / fs
    (ln,) = ax.plot(xvals, data, animated=True)
    ax.set_xlim((0, n_samples / fs))
    ax.set_ylim(ylims)

    # Generate the boolean signal dots
    # These should be stacked in the bottom left hand corner of the plot, and each dot should be aligned with the name of that boolean signal
    # The dots should be a hollow black circle if False, and a filled green circle if True
    bool_dots = []
    xcorner_val_text = xvals[int(len(xvals) / 30)]
    xcorner_val = xvals[int(len(xvals) / 5)]
    ylim_range = ylims[1] - ylims[0]

    if len(bool_val_names) > 0:
        for i, name in enumerate(bool_val_names):
            yval = ylims[0] + ylim_range * 0.05 * (i + 1)

            bool_dots.append(
                ax.plot(
                    xcorner_val, yval, "o", color="C0", markersize=10, animated=True
                )[0]
            )

            ax.annotate(
                name + ":",
                (xcorner_val_text, yval),
                ha="left",
                va="center",
                # animated=True,
            )

    # Prepare the text annotations in the top left
    frame_text = ax.annotate(
        "0",
        (0, 1),
        xycoords="axes fraction",
        xytext=(10, -10),
        textcoords="offset points",
        ha="left",
        va="top",
        animated=True,
    )

    # Add all the animated artists to the blit manager
    bm = BlitManager(fig.canvas, [ln, frame_text] + bool_dots)

    # Make sure our window is on the screen and drawn
    plt.show(block=False)
    plt.pause(1)

    # Check if we cna read queue size
    try:
        qsize = data_queue.qsize()
        qsize_readable = True
    except NotImplementedError:
        qsize_readable = False
        warn("Queue size is not readable on this platform")

    # Loop to update the plot
    current_timeout = 10
    while not exit_event.is_set():
        # Read data from the queue, without blocking.
        # Will raise the "empty" exception if it's empty, or the ValueError exception if it's closed.
        try:
            signal_vec, bool_vals, text_vals = data_queue.get(
                timeout=current_timeout
            )  # tuple of (signal vec, bool vals, text vals), or empty if end
            current_timeout = (
                0.1  # reduce timeout to 100 ms after first successful read
            )
        except Empty:
            continue
        except (ValueError, BrokenPipeError):
            print("queue closed")
            break

        # Update the animated line
        ln.set_ydata(signal_vec)

        # Update the time to be shown
        if (time.time() - tic) > 1:
            time_txt = f"Time (sec): {time.time() - tic:.2f}"

        # Update the boolean dots
        if len(bool_vals) > 0:
            for i, val in enumerate(bool_vals):
                if val:
                    bool_dots[i].set_color("green")
                else:
                    bool_dots[i].set_color("red")

        if qsize_readable:
            qsize = data_queue.qsize()
        else:
            qsize = "N/A"
        queue_txt = f"queue sz: {qsize}"

        # # Update the user-specified text annotations
        text_txt = "\n".join(
            [f"{name}: {val}" for name, val in zip(text_val_names, text_vals)]
        )

        frame_text.set_text("\n".join([time_txt, text_txt, queue_txt]))

        bm.update()

    plt.close(fig)
    return
