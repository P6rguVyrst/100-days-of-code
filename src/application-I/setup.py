from setuptools import setup, find_packages

requirements = [
    'requests'
]
test_requirements = [
    'pytest',
]
setup_requirements = [

]
long_description = ''

setup(
    name='project',
    version='0.1.0',
    description='',
    long_description=long_description,
    url='',
    author='Toomas Ormisson',
    author_email='toomas.ormisson@gmail.com',
    packages=find_packages(include=['project']),
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords= [
        'testing'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
