# Generate RISC-V Project

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_riscv/dev/docs/gen_riscv_logo.png" width="25%">

**gen_riscv** is tool for generation of RISC-V project.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_riscv python checker](https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python_checker.yml) [![gen_riscv package checker](https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_riscv.svg)](https://github.com/vroncevic/gen_riscv/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_riscv.svg)](https://github.com/vroncevic/gen_riscv/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Code coverage](#code-coverage)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_riscv/dev/docs/debtux.png)

[![gen_riscv python3 build](https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/gen-riscv/)**.

You can install by using pip

```bash
#python3
pip3 install gen-riscv
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_riscv/releases/)** download and extract release archive.

To install **gen_riscv** type the following

```bash
tar xvzf gen_riscv-x.y.z.tar.gz
cd gen_riscv-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_riscv-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_riscv_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_riscv_run.py /usr/local/bin/gen_riscv_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_riscv/releases)** download and extract release archive.

To install **gen_riscv** locate and run setup.py with arguments

```bash
tar xvzf gen_riscv-x.y.z.tar.gz
cd gen_riscv-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_riscv** requires next modules and libraries

- [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Tool structure

**gen_riscv** is based on OOP.

Generator structure

```bash
    gen_riscv/
        ├── conf
        │   ├── gen_riscv.cfg
        │   ├── gen_riscv.logo
        │   ├── gen_riscv_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── cflags.template
        │       ├── csflags.template
        │       ├── main.template
        │       ├── Makefile.template
        │       ├── objects.template
        │       ├── odflags.template
        │       ├── sources.template
        │       └── toolchain.template
        ├── __init__.py
        ├── log/
        │   └── gen_riscv.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_riscv_run.py

    6 directories, 18 files
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_riscv/__init__.py` | 71 | 14 | 80% |
| `gen_riscv/pro/__init__.py` | 59 | 6 | 90% |
| `gen_riscv/pro/read_template.py` | 53 | 4 | 92% |
| `gen_riscv/pro/write_template.py` | 62 | 5 | 92% |
| **Total** | 245 | 29 | 88% |

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_riscv/badge/?version=latest)](https://gen-riscv.readthedocs.io/projects/gen_riscv/en/latest/?badge=latest)

More documentation and info at

- [gen_riscv.readthedocs.io](https://gen-riscv.readthedocs.io/en/latest/)
- [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 - 2024 by [vroncevic.github.io/gen_riscv](https://vroncevic.github.io/gen_riscv)

**gen_riscv** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_riscv/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
