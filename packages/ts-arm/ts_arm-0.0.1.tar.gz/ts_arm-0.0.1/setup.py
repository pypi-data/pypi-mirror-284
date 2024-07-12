from setuptools import setup, find_packages


setup(
    name='ts_arm',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ts_arm': ['synthetic_F1_array.npy'],
    },
    url='https://github.com/DL4mHealth/TS-Contrastive-Augmentation-Recommendation',
    license='MIT',
    author='Ziyu Liu',
    author_email='ziyu.liu2@student.rmit.edu.au',
    description='Guidelines for Augmentation Selection in Contrastive Learning '
                'for Time Series Classification',
    install_requires=[
        'numpy',
        'scikit_learn',
        'scipy',
        'setuptools',
        'statsmodels',
        'tqdm',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Science/Research'
    ],
)
