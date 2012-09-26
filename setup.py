from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='xiru.alchemyform',
      version=version,
      description="A CRUD implementation using Plone, SQLAlchemy and z3c.form",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone sqlalchemy z3c.form',
      author='Fabiano Weimar dos Santos',
      author_email='xiru@xiru.org',
      url='https://github.com/xiru/xiru.alchemyform',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['xiru'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'five.grok',
          'z3c.saconfig',
          'MySQL-python',
          'plone.directives.form',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
