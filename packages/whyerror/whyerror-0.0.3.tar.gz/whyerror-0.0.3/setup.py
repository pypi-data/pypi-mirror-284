from setuptools import setup, find_packages

setup(
    name='whyerror',
    version='0.0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'google-generativeai',
        'click',
        'python-dotenv',
        'keyring'
    ],
    entry_points={
        'console_scripts': [
            'whyerror=whyerror.cli:whyerror',
        ],
    },
)
