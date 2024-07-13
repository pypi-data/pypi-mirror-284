from setuptools import setup, find_packages

setup(
    name='haber-devops',
    version='1.0.0',
    description='CLI tool for managing AWS resources',
    author='Shweta Jha',
    author_email='shweta.jha@haberwater.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'boto3',
        'docker',
        'PyYAML',
        'paramiko'
    ],
    entry_points={
        'console_scripts': [
            'haber-devops=haberdevops.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
