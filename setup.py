from setuptools import setup
from querycount import __version__

url = "https://github.com/enzoclicoh/clicoh-querycount/{0}".format(__version__)

setup(
    name="django-querycount-clicoh",
    version=__version__,
    author="Clicoh",
    author_email="banckend_test@clicoh.com.ar",
    description=("Middleware that Prints the number of DB queries to the runserver console."),
    install_requires=[],
    license="MIT",
    keywords="django querycount database performance",
    url=url,
    packages=[
        "querycount",
    ],
    long_description="this project gives you a middleware that"
    "prints DB query counts in Django's runserver console output.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        "Topic :: Utilities",
    ],
)
