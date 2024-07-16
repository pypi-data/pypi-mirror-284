from setuptools import setup, find_packages

setup(
    name='aes-tool',
    version='0.1.0',
    description='Advanced AES Encryption Decyption Toolkit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Babar Ali Jamali',
    author_email='babar995@gmail.com',
    url='https://github.com/babaralijamali/aes-tool',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pycryptodome',
    ],
)
