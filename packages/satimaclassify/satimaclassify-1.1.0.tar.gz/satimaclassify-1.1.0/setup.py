import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='satimaclassify',
    version='1.1.0',
    author='b0814',
    author_email='b0814@n-koei.co.jp',
    description='A package for satellite image classification(SatImaCla)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/satellite_image_classification',
    packages=setuptools.find_packages(),
    install_requires=[
        'rasterio',
        'numpy',
        'scikit-learn',
        'fiona',
        'matplotlib',
        'pandas',
        'joblib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
