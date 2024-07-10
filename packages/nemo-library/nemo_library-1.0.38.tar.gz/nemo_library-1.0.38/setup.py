from setuptools import setup, find_packages

setup(
    name='nemo_library',
    version='1.0.38',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'nemo_library': ['sql_keywords.json'],
    },
    install_requires=[
        'requests','pandas'
    ],
    author='Gunnar Schug',
    author_email='GunnarSchug81@gmail.com',
    description='A library for uploading data to and downloading reports from NEMO cloud solution',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',    
    classifiers=[
        'Programming Language :: Python :: 3.12',
    ],
    project_urls={
        'Github': 'https://github.com/H3rm1nat0r/nemo_library',  
        'NEMO': 'https://enter.nemo-ai.com/nemo/'
    }
)
