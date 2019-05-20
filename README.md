# Code_parser
Code parser is a first Otus homework.
It'll give some stats on your project: total number of unique words, most common word, functions and most common word in functions.
##Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Code parser.

```pip install code_parser```
##Usage
```python3 -m code_parser [-p PROJECT_PATH] [-e EXCLUDET_DIRS]```
##Example
```python3 -m code_parser -p /User/myproject/new_project -e venv,some_lib,other_lib```

```
Found 22 functions
Most common is get, used 6 times
Found 309 words, unique 55
Most common is names, used 44 times
```
##Requirements
```nltk==3.4.1```
```six==1.12.0```


