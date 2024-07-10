from setuptools import setup, find_packages

setup(
    name='vision_kais',
    version='0.0.1',
    description='vision function written by kais',
    author='misil han',
    author_email='coko980715@gmail.com',
    install_requires=['socket', 'requests',],
    packages=find_packages(exclude=[]),
    keywords=['kais', 'vision'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
)
