from setuptools import setup, find_packages

# Update these:
name = 'pexception'  # This needs to be the same name as the repo
description = 'Pretty print exception stack traces.'
long_description = description


setup(
    author='Ryan Chui',
    author_email='ryan.w.chui@gmail.com',
    description=description,
    license='MIT',
    long_description=long_description,
    name=name,
    packages=find_packages(),
    url='https://github.com/rchui/' + name,
    version='0.0.1',
    zip_safe=True,
    install_requires=[],
    setup_requires=[],
)
