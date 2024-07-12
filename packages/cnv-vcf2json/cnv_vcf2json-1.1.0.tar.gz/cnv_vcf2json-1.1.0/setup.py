from setuptools import setup, find_packages

setup(
    name='cnv_vcf2json',
    version='1.1.0',
    author='Khaled Jumah',
    author_email='khalled.joomah@yahoo.com',
    description='Converts the structural variants VCF file into JSON file',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cnv-vcf2json = vcf_converter.cnv_vcf2json:cnv_vcf2json'
        ]
    },
    install_requires=[
        'jsonschema'  # Added jsonschema dependency
    ],
)
