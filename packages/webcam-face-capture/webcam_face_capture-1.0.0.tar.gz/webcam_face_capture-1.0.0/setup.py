from setuptools import setup, find_packages

setup(
    name='webcam_face_capture',
    version='1.0.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'opencv-python',
    ],
    entry_points={
        'console_scripts': [
            'webcam-face-capture = main:main',
        ],
    },
    author='Ranjit',
    author_email='ranjitmaity95@gmail.com',
    description='A utility to capture faces from webcam and save them in grayscale',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
