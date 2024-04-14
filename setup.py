from setuptools import setup, find_packages

setup(
    name='donkey_utils',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A Python library for handling DonkeyCar data.',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas', 'matplotlib', 'Pillow','tarfile'],
    url='http://pypi.python.org/pypi/DonkeyUtils/',
    author='Your Name',
    author_email='your.email@example.com'
)
