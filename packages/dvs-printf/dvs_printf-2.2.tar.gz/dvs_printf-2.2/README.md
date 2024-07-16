<div align="center">

<h3>Simple & Dynamic Console Animation Styles for Python</h3>
  
[![PyPI Version](https://badge.fury.io/py/dvs-printf.svg)](https://badge.fury.io/py/dvs-printf)
[![Build Status](https://github.com/dhruvan-vyas/dvs_printf/actions/workflows/module_test.yml/badge.svg)](https://github.com/dhruvan-vyas/dvs_printf/actions)
[![GitHub Release (latest by date)](https://img.shields.io/github/v/release/dhruvan-vyas/dvs_printf)](https://github.com/dhruvan-vyas/dvs_printf/releases/tag/v2.2)<br>
![Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/dhruvan-vyas/dvs_printf/blob/main/LICENSE)
[![PEP8](https://img.shields.io/badge/PEP8-compliant-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

<a href="https://github.com/dhruvan-vyas/dvs_printf">
  <img src="https://github.com/dhruvan-vyas/dvs_printf/blob/main/card.png?raw=true">
</a>

</div>

Enhanced way to handle console output for python projects. The module offers **printf** style animation 
functions designed to improve the visual appearance of terminal-based Python projects. Key features 
include different animation styles, customizable speeds, and flexible formatting options.

<br>

# Installation
choose the appropriate one-liner command according to your system. \
ensure a Straight Forward setup process. 

### Linux / macOS
```bash
pip3 install dvs_printf
``` 
```bash
python3 -m pip install dvs_printf
```

### Windows
```bash
pip install dvs_printf
```
```bash
python -m pip install dvs_printf
```

### Clone the Repository
```bash
git clone https://github.com/dhruvan-vyas/dvs_printf.git
```

<br>

# Documentation

<a style="text-decoration:none" href="https://github.com/dhruvan-vyas/dvs_printf?tab=readme-ov-file#printf-function">**printf**</a>: 
The core function of the module, allowing users to apply various animation styles to their values. Supports different data types 
(**string, int, float, list, set, tuple, dict, Any,** ...) with (**custom object**) and classes (**numpy, tensorflow, pytorch, pandas**) 
as input. Users can choose from a range of animation styles, including typing, async, headline, center, left, right, and more. 
Customizable parameters include **style, speed, delay, getmat**, and the **stay** option to make the printed values stay or disappear.

<a style="text-decoration:none" href="https://github.com/dhruvan-vyas/dvs_printf?tab=readme-ov-file#dvs_printfinit-method">**dvs_printf.init**</a>: A dynamic initializer for printf that allows users to preset parameters for consistent usage. <br>
Priority order for setting parameters: **printf's keywords** > **Setter Variables** > **dvs_printf.init's keywords** > **Defaults**.<br>
More details on GitHub README.

<a style="text-decoration:none" href="https://github.com/dhruvan-vyas/dvs_printf?tab=readme-ov-file#showLoading-function">**showLoading**</a>: 
A function for creating loading bars in the terminal, useful for waiting times during tasks like downloading files or running background functions. 
Users can customize loading text, loading bar, and other parameters.

<a style="text-decoration:none" href="https://github.com/dhruvan-vyas/dvs_printf?tab=readme-ov-file#list_of_str-function">**list_of_str**</a>: 
A supplementary *wrapper function* used by *printf* to create new list based on input values. 
Can handle various data types and optionally convert matrices into list of strings by rows.

<br>

***

The <a style="text-decoration:none" href="https://github.com/dhruvan-vyas/dvs_printf#dvs_printf">GitHub README</a> 
file includes clear examples, code snippets, videos, and explanations to assist users in implementing the module effectively. 
All links above lead to the same file.
