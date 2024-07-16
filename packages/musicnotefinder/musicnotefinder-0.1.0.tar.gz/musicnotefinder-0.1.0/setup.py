from setuptools import setup, find_packages

setup(
    name='musicnotefinder',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'librosa',
        'numpy',
        'soundfile',
        'aubio',
        'scipy',
        
    ],
    author='karthikeyan nagarajan',
    author_email='keyan156@gmail.com',
    description='A library for analyzing audio files and detecting musical notes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/musicnotefinder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
