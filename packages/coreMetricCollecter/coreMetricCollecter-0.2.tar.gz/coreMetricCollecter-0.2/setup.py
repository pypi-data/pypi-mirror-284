from setuptools import setup, find_packages

setup(
    name='coreMetricCollecter',
    version='0.2',
    description='A Prometheus metrics collector for thread counts',
    author='coreteam',
    author_email='coreteam@example.com',
    packages=find_packages(),
    install_requires=[
        'prometheus_client',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)