import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyBNG",
    version="0.1.8",
    author="Mohamed Shahawy",
    author_email="mohamedshahawy@icloud.com",
    description="A library to convert BNG/OSNG coordinates ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThunderStruct/PyBNG",
    packages=setuptools.find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Other Audience',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux'
    ],
    keywords='gis mapping coordinates grid-reference mapping ordiance-survey lat-long bng all-numeric',
    python_requires='>=3.6',
    install_requires=['OSGridConverter']
)