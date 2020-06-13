# wxcalc-example
Very basic calculator using wxWidgets in Python

This isn't anything sophisticated, just a very simple calculator application done to serve as a tiny example of how to get started with wxWidgets in Python.  Personally I find wxWidgets nice to work with and it gives a clean native look wherever you run it.  The downsize is the pip package to get going is a good 70MB in size.

To get up and running I'll assume you want to run this from a Python virtual environment and you've got the executable 'python3' available on a command line:

python3 -m venv venv-wxcalc
./venv-wxcalc/bin/activate  # Linux/macOS
.\venv-wxcalc\scripts\activate # Windows
pip install wxwidgets # -or-
pip -r requirements.txt

To run:
python src/main/py
