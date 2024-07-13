from setuptools import setup, find_packages

setup(
    name='snipdb',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A lightweight JSON database',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='simpx',
    author_email='simpxx@gmail.com',
    url='https://github.com/simpx/atomdb',
    license='MIT',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
)

