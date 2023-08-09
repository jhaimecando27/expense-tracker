# Expense Tracker

> **Note**
Won't be maintaining the original final project output. I will be creating another version of this type of project.

##### Table of Contents
- [Requirements](#requirements)
- [Project Layout](#project-layout)
- [Usage](#usage)
- [References](#references)
- [License](#license)

##### Requirements
1. Python
2. Flask

##### Project Layout

    ├── app/
    │   ├── __init__.py
    │   ├── db.py
    │   ├── schema.sql
    │   ├── auth.py
    │   ├── main.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── auth/
    │   │   │   ├── login.html
    │   │   │   └── register.html
    │   │   └── main/
    │   │       ├── index.html
    │   │       └── update.html
    │   └── static/
    │       └── images/
    │           └── favicons/
    │               ├── 32.png
    │               └── 96.png
    └── run.py

1. `app/` - Python package containing your application code and files.
2. `app/__init__.py` - it contains the application factory, and it tells Python that the application's directory should be treated as a package.
3. `app/db.py` - The application used SQLite database to store users and their expenses.
4. `app/schema.sql` - Contains SQL commands to create empty tables.
5. `app/auth.py` - Authentication system (Login, Register, etc)
6. `app/main.py` - It contains the application's main functionalities that is related to expense tracker
7. `templates/` - The application used Jinja to render the UI.
8. `static/` - It contains images, javascripts and styles.
9. `run.py` - It contains short python script to run the application

##### Usage
1. Initialize the database
```
$ flask init-db
```
2. Run the server
```
$ python run.py
```

##### References
1. [Flask](https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/)
2. [CS50x-2022 Week 9](https://cs50.harvard.edu/x/2022/weeks/9/)


##### License

MIT License

Copyright (c) 2012 Jhaime Cando

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
