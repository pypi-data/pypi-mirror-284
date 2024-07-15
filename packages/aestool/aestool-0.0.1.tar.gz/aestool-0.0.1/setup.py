from setuptools import setup, find_packages

setup(
    name='aestool',
    version='0.0.1',
    description='A simple AES encryption and decryption tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Babar Ali Jamali',
    author_email='babar995@gmail.com',
    url='https://github.com/babaralijamali/aestool',
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
    entry_points={
        'console_scripts': [
            'aestool=aestool.aestool:main',
        ],
    },
)
