from setuptools import setup

setup(
    name='colorednoise',
    version='1.0',
    description='Generate Gaussian (1/f)**beta noise (e.g. pink noise)',
    long_description="""
        Generate gaussian distributed noise with a power law spectrum.
        Based on the algorithm in 
            Timmer, J. and Koenig, M.:
            On generating power law noise. 
            Astron. Astrophys. 300, 707-710 (1995)
    """,
    classifiers=[
      'Development Status :: 1 - Production',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
      'Topic :: Scientific/Engineering'
    ],
    keywords='1/f flicker power-law correlated colored noise generator',
    url='http://github.com/felixpatzelt/colorednoise',
    author='Felix Patzelt',
    author_email='felix@neuro.uni-bremen.de',
    license='MIT',
    py_modules=['colorednoise'],
    install_requires=[
        'numpy',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
)