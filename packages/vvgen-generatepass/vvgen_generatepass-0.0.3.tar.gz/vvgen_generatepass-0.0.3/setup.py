from setuptools import setup, find_packages

setup(
    name='vvgen_generatepass',
    version='0.0.3',  # Убедитесь, что версия соответствует текущей
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    author='Nikita',
    author_email='firi8228@gmail.com',
    description='A secure password generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)