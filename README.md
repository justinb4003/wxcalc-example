# wxcalc-example
Very basic calculator using wxWidgets in Python

This isn't anything sophisticated, just a very simple calculator application done to serve as a tiny example of how to get started with wxWidgets in Python.  Personally I find wxWidgets nice to work with and it gives a clean native look wherever you run it.  The downsize is the pip package to get going is a good 70MB in size.

To get up and running I'll assume you want to run this from a Python virtual environment, you've cloned the repository, and you've got the executable 'python3' available on a command line:

```
python3 -m venv venv-wxcalc
```
Activate your virtual environment (Linux/macOS):
```
./venv-wxcalc/bin/activate
```
... Windows:
```
.\venv-wxcalc\scripts\activate # Windows
```

To install the necessary packages to run the application you would generally execute:
```
pip -r requirements.txt
```
But given the idea is to show you how to use wxWidgets in your own Python projects all you really need to install is 'wxwidgets' and the necessary dependencies will get pulled in:
```
pip install wxwidgets
```


To run:
```
python src/main.py
```
