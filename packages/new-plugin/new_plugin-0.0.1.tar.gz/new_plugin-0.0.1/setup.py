from setuptools import setup, find_packages

setup(
    name='new_plugin',
    version='0.0.1',
    description='LOL KEK CHEBUREK',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points= {
        'testy': [ 'new_plugin = new_plugin' ],
    },
    install_requires=[
        'django',
        'testy',
        'rest_framework',
    ],
)