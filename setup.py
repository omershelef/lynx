from setuptools import setup, find_packages
import os


f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read().strip()
f.close()



setup(name='lynx',
      version='0.2.4',
      description = "Python configuration library",
      license="The MIT License (MIT)",
      url = "https://github.com/omershelef/lynx/",
      long_description = long_description,
      author = "Omer Shelef",
      author_email = "shlaflaf@gmail.com",
      packages=find_packages(
        where='.'
      ),
      tests_require=['pytest'],
      test_suite="tests.test_lynx.run_tests"
      )
