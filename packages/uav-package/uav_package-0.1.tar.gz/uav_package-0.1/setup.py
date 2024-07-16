from setuptools import setup, find_packages

setup(
    name='uav_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'geopy',
        'shapely'
    ],
    author='Yazar Adınız',
    author_email='email@example.com',
    description='UAV data processing and scoring package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kullaniciadi/uav_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
