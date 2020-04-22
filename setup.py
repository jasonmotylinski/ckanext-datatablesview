from setuptools import setup, find_packages


version = '0.0.1'
setup(
    name='ckanext-datatablesview',
    version=version,
    description="Customized datatables view from external databases",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Fadeit Aps',
    author_email='jason@motylinski.com',
    url='https://github.com/jasonmotylinski/ckanext-datatablesview',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.datatablesview'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        datatablesview=ckanext.datatablesview.plugin:DataTablesView
    ''',
)
