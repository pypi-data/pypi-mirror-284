from setuptools import setup, find_packages

setup(
    name='core_metrics_collector',
    version='0.1',
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