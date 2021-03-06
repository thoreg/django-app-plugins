from setuptools import setup, find_packages

setup(
    name='django-app-plugins',
    version='0.1.2',
    description='reusable django application for writting pluggable reusable django applications',
    author='Doug Napoleone, Thomas Rega',
    author_email='doug.napoleone@gmail.com, thoreg@gmail.com',
    url='https://github.com/thoreg/django-app-plugins',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {
        'app_plugins': ['templates/app_plugins/*.html'],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
