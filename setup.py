#!/usr/bin/env python
from distutils.core import setup

setup(name='splittar',
        version='0.2',
        description="create multiple tar files with a specified maximum size",
        long_description="""splittar allows you to create one or more tar files
from a set of data where each of the generated tar files is less than a
specified maximum size.
 
Each tar file is a proper, self-contained tar file.  Other methods of
backing up data to removable media requires a tar file to be split, making
tar file n useless without files 1,...,n-1.
 
splittar was written to backup large amounts of data that spanned multiple
DVDs while allowing for each DVD to be useful on its own.""",
        author="Chris AtLee",
        author_email="chris@atlee.ca",
        url="http://atlee.ca/blog/software/splittar/",
        download_url="http://atlee.ca/software/splittar/splittar_0.2.tar.gz",
        scripts=['splittar',],
        license='GPL',
        platforms=['Linux',],
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux', # Although it may work on others?
            'Programming Language :: Python',
            'Topic :: Utilities',
            'Topic :: System :: Archiving',
            ]
        )
