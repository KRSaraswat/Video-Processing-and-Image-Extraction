from setuptools import setup, find_packages

setup(
    name='video_image_pipeline',
    version='0.1',
    description='A utility package for video frame extraction and image processing.',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'moviepy',
        'Pillow',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
