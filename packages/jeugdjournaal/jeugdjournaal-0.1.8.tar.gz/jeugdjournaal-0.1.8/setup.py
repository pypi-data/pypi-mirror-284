from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='jeugdjournaal',
    version='0.1.8',
    author='hcr5',
    author_email='hcr5.hcr@gmail.com',
    description='Python library to interact with the jeugdjournaal API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hcr5/jeugdjournaalpy',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT'
)
