from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geofinder_vt",  # Replace with your own package name
    version="0.2.10",
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
        'affine==2.4.0',
        'attrs==23.1.0',
        'babel==2.12.1',
        'certifi==2023.5.7',
        'charset-normalizer==3.1.0',
        'click==8.1.3',
        'click-plugins==1.1.1',
        'cligj==0.7.2',
        'colorama==0.4.6',
        'contextily==1.3.0',
        'contourpy==1.0.7',
        'customtkinter==5.1.3',
        'cycler==0.11.0',
        'darkdetect==0.8.0',
        'decorator==4.4.2',
        'descartes==1.1.0',
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
        'importlib-metadata==6.6.0',
        'importlib-resources==5.12.0',
        'joblib==1.2.0',
        'kiwisolver==1.4.4',
        'lxml==4.9.2',
        'moviepy==1.0.3',
        'numpy==1.24.3',
        'opencv-python==4.7.0.72',
        'packaging==23.1',
        'pandas==2.0.1',
        'proglog==0.1.10',
        'pyee==9.1.0',
        'pyexiftool==0.4.13',
        'pyparsing==3.0.9',
        'pyperclip==1.8.2',
        'pyproj==3.5.0',
        'python-dateutil==2.8.2',
        'pytz==2023.3',
        'pywin32==306',
        'rasterio==1.3.7',
        'ratelim==0.1.6',
        'requests==2.31.0',
        'shapely==2.0.1',
        'six==1.16.0',
        'snuggs==1.4.7',
        'tqdm==4.65.0',
        'typing-extensions==4.6.0',
        'tzdata==2023.3',
        'urllib3==1.26.6',
        'xmltodict==0.13.0',
        'xyzservices==2023.5.0',
        'zipp==3.15.0'

    ],
)