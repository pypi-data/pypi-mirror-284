from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geofinder_vt",  # Replace with your own package name
    version="0.2.9",
    author="Your Name",
    author_email="vaidhyanathan@vt.edu",
    description="A brief description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathan846/geofindervt",  # Replace with the URL of your project
    packages=find_packages(include=["geofinder_vt", "geofinder_vt.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=[
        'babel==2.12.1',
        'certifi==2023.5.7',
        'charset-normalizer==3.1.0',
        'ffmpeg-python==0.2.0',
       'fonttools==4.39.4',
        'future==0.18.3',
        'geocoder==1.38.1',
        'geopandas==0.13.0',
        'geopy==2.3.0',
        'gpmf==0.1',
        'gpxpy==1.5.0',
        'idna==3.4',
        'imageio==2.29.0',
        'imageio-ffmpeg==0.4.8',
        'lxml==4.9.2',
        'moviepy==1.0.3',
        'numpy==1.24.3',
        'opencv-python==4.7.0.72',
        'packaging==23.1',
        'pandas==2.0.1',
        'python-dateutil==2.8.2',
        'pytz==2023.3',
        'requests==2.31.0',
        'tqdm==4.65.0',
        'typing-extensions==4.6.0',
        'tzdata==2023.3',
        'urllib3==1.26.6',
        'xmltodict==0.13.0',
    ],
)