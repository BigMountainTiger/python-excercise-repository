from setuptools import setup

setup(
    name='loyalty',
    version='0.1.0',
    py_modules=['cli'],
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'loyalty = cli:cli'
        ]
    }
)
