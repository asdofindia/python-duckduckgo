from setuptools import setup
from duckduckgo import __version__

long_description = open('README.rst').read()

setup(name='duckduckgo3',
      version=__version__,
      py_modules=['duckduckgo'],
      description='Library for querying the DuckDuckGo API',
      author='Akshay S Dinesh',
      author_email='asdofindia@gmail.com',
      license='BSD',
      url='http://github.com/asdofindia/python-duckduckgo/',
      long_description=long_description,
      platforms=['any'],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
                   ],
      entry_points={'console_scripts':['ddg = duckduckgo:main']},
      )
