from setuptools import setup, find_packages

setup(
    name='karrotcapital.spiderswap',
    version='1.0.2',
    description='A package for interacting with the SpiderSwap API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dutch - Karrot Capital',
    author_email='dutch@karrot.capital',
    url='https://docs.karrot.capital',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.7.4',
        'solana>=0.21.0',
        'base58>=2.1.0',
        'solders',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)