from setuptools import setup

setup(
    name='repoman',
    version='0.1',
    description='Repository Update Manager',
    author='Brad Osgood',
    author_email='bosgood@gmail.com',
    zip_safe=False,
    include_package_data=True,
    url='http://github.com/bosgood/repoman',
    install_requires=[
        'pyyaml==3.10'
    ],
    dependency_links=[],
    platforms=["any"],
)
