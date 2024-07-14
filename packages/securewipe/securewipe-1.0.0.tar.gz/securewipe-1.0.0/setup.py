from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='securewipe',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'securewipe-cli = securewipe.cli:main',
        ],
    },
    description='A Python package for securely wiping files or folders.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Fidal',
    author_email='mrfidal@proton.me',
    url='https://github.com/Bytebreach/securewipe',
    license='MIT',
)
