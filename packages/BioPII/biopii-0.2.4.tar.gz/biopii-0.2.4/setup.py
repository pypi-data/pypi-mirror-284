from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='BioPII',
    version='0.2.4',
    author='Seth Ockerman',
    author_email='ockermas@mail.gvsu.edu',
    description='BioPII (Biology Parallel Integral Image) is a Python package for performing sliding window analysis (SWA) on biological images.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OckermanSethGVSU/BioPII',
    packages=find_packages(),
    py_modules=['BioPII'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: GPU :: NVIDIA CUDA',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Biology, Integral Image, Sliding Window, HPC',
    install_requires=[
        'numpy',
        'opencv-python',
    ],
      extras_require={
        'GPU-Support': ['cupy']
    },
)

