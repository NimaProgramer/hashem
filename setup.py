from setuptools import setup, find_packages

setup(
    name='hashemPack',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'MetaTrader5',
        'numpy',
        'statistics',
        'requests',
        'telebot',
    ],
    author='NimaDalir',
    author_email='n.dalir1998@gmail.com',
    description=' "Hashem Trader" package highlights it as a versatile tool for developing and connecting to the MetaTrader 5 platform for automated trading bot creation.',
    long_description=open('README.md').read(),
    url='https://github.com/NimaProgramer/hashem/blob/main/README.md',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.0',
)
