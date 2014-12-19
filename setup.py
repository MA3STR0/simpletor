from distutils.core import setup
setup(
    name = 'simpletor',
    packages = ['simpletor'], # this must be the same as the name above
    version = '0.1',
    description = 'Tiny lib to make all Python network connections through Tor',
    author = 'Anton C',
    author_email = 'anton@maestr0.com',
    url = 'https://github.com/MA3STR0/simpletor',
    download_url = 'https://github.com/MA3STR0/simpletor/tarball/v0.1',
    keywords = ['tor', 'proxy', 'anonymous'],
    classifiers = [],
    install_requires=[
        "pysocks",
        "stem"
    ],
)
