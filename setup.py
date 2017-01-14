import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-simplepush",
    version="0.10",
    description="A webpush notifications plugable app for Django",
    url='https://github.com/subhajeet2107/django-simplepush',
    license='BSD',
    author='Subhajeet Dey',
    author_email='subhajeet2107@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    download_url = 'https://github.com/subhajeet2107/django-simplepush/archive/master.zip',
    classifiers=[
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=['pywebpush==0.6.1']
)