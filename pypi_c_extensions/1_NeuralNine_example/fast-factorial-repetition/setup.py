from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension(
            name="fast_factorial_repetition",
            sources=["implementation/fast_factorial_repetition.c"]
        )
    ]
)
