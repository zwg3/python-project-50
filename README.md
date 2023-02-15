### Hexlet tests and linter status:
![https://github.com/zwg3/python-project-50/actions/workflows/Project-50-ci.yml/badge.svg](https://github.com/zwg3/python-project-50/actions/workflows/Project-50-ci.yml/badge.svg)
[![Actions Status](https://github.com/zwg3/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/zwg3/python-project-50/actions)
<a href="https://codeclimate.com/github/zwg3/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/ee26a262e35fc35b327f/maintainability" /></a>
<a href="https://codeclimate.com/github/zwg3/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/ee26a262e35fc35b327f/test_coverage" /></a>

### Requirements
- python 3.10
- pyyaml = 6.0

### Installation:
In terminal type the following commands from the package directory:
- make install
- make build
- make package-install

### Usage:
The program is used to find differences between two files (.json or .yml format).
After the installation use the following commands:
- gendiff -f stylish <filepath1> <filepath2> (gets you a default difference)
- gendiff -f json <filepath1> <filepath2> (gets you a json-formated difference)
- gendiff -f plain <filepath1> <filepath2> (gets you a plain difference)
Note: if you do not specify the format (via -f), stylish format will be used as a default one.

### Basic info
[![asciicast](https://asciinema.org/a/i8tdenKgicgJUf5qPmWQwfmaX.svg)](https://asciinema.org/a/i8tdenKgicgJUf5qPmWQwfmaX)

### Stylish format output
[![asciicast](https://asciinema.org/a/8BUWuHAapNOQmhMYoMUzGB9iv.svg)](https://asciinema.org/a/8BUWuHAapNOQmhMYoMUzGB9iv)

### Plain format output
[![asciicast](https://asciinema.org/a/bPSPEtGk3AIwzNONDrzPPfuNa.svg)](https://asciinema.org/a/bPSPEtGk3AIwzNONDrzPPfuNa)

### Json format output
[![asciicast](https://asciinema.org/a/oufXaWoxmjtVl4chZg91Ec0zL.svg)](https://asciinema.org/a/oufXaWoxmjtVl4chZg91Ec0zL)

