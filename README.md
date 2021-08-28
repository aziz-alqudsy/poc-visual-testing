# poc-visual-testing
The proof of concept visual testing.
## prerequisite
1. create virtual environment
```sh
$ python -m venv venv
$ source venv/bin/activate
```
2. update and install python modules
```sh
$ pip install --upgrade pip
$ pip install selenium pytest pytest-html pillow
$ pip freeze > requirements.txt
```
3. make local web project. in my case, I develop 2 different register pages using next.js.

## how to run
```sh
$ python -m pytest  -sv --html reports/report.html
```

## result
Check image in `./screenshots/grid_registerpage.png`. on the red grid is the different element compares to production page.
