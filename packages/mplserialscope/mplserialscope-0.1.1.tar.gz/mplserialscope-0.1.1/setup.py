from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

setup(
    name='mplserialscope',
    version='0.1.1',
    license='MIT or Allen Institute Software License',
    description='A utility to take continuous serial output (i.e. from an Arduino) and plot it in real-time with matplotlib ',
    author='Jonah Pearl',
    author_email='jonahpearl@g.harvard.edu',
    url='https://github.com/jonahpearl/mpl_serial_to_oscope',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=[
        'numpy',
        'matplotlib',
        'PyQt5',
    ],
)