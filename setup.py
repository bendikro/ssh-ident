#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

import ssh_ident


setup(name='ssh-ident',
      version=ssh_ident.__version__,
      description="Start and use ssh-agent and load identities as necessary.",
      long_description="Start and use ssh-agent and load identities as necessary.",
      url='https://github.com/ccontavalli/ssh-ident',
      license="BSD",
      packages=find_packages(),
      namespace_packages=['ssh_ident'],
      entry_points={'console_scripts':
                    ['ssh_ident_ssh = ssh_ident.ssh_ident:main',
                     'ssh_ident_cli = ssh_ident.ssh_ident_cli:main'
                    ]
      },
      scripts=[
          'scripts/ssh-ident-completion.bash',
          'scripts/ssh_ident.sh',
      ],
      zip_safe=False,
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: POSIX'
      ])
