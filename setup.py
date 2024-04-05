# coding: utf-8

"""
    Dti.TaxCore.VSDC.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dti_tax_core_vsdc_api_client_swagger"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]


setup(
    name=NAME,
    version=VERSION,
    description="Dti.TaxCore.VSDC.Api",
    author="agajic-modoolar",
    author_email="aleksandar.gajic@modoolar.com",
    license='MIT',
    url="https://github.com/modoolar/dti_tax_core_vsdc_api_client_swagger",
    keywords=["Swagger", "Dti.TaxCore.VSDC.Api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501
    """
)
