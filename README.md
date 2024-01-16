# FindLang

FindLang is a standalone Language Identification (LangID) tool based on the original `findid.py`. The original tool was mainly available for Python 2 and included both Python 2 and Python 3 code, making it challenging to compile as a whole library. The compilation process was not dynamic, especially when dealing with both Python 2 and Python 3 code.

This project aims to provide a Python 3 version of the `findid.py` tool by translating the Python 2 code, removing all Python 2-specific code, and focusing on a clean Python 3 implementation. This modification enables easy compilation of the library, making it suitable for integration into standalone applications, such as through PyOxidizer. 
Note:  (PyOxidizer is a utility that can turn Python code into a single executable file that can be run on systems without a Python interpreter installed. I used it for personal purposes, but it is not required to use this library.)

## Features

- Standalone Language Identification tool for Python 3.
- Based on the original `findid.py` tool, with Python 2 code translated and removed.
- Simplified and clean Python 3 implementation.
- Suitable for dynamic compilation and integration into standalone applications.

## Usage

The simplest way to use ``findlang`` is as a command-line tool, and you can 
invoke using ``python findlang.py``. If you installed ``findlang`` as a Python 
module (e.g. via ``pip install findlang``), you can invoke ``findlang`` instead of 
``python findlang.py`` (the two are equivalent).  This will cause a prompt to 
display. Enter text to identify, and hit enter::

```bash
$ python findlang.py
>>> This is a test
('en', 0.99999999099035441)
>>> Questa e una prova
('it', 0.98569847366134222)
```
