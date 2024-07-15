# Arbitrium_interface/setup.py
from setuptools import setup, find_packages

setup(
    name='Arbitrium_interface',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
        'django-admin-interface',
    ],
    description='A custom Django admin interface',
    author='Arnav',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    package_data={
        'Arbitrium_interface': ['fixtures/admin_interface_theme.json'],
    },
)
