# Archiving Microservice
===========

Version 1 of the SignEasy Archiving Microservice.

Index
---
- [Stack Details](#stack-details)
- [Development Setup](#dev-setup)
- [API Documentation](#api-documentation)
- [ERROR CODE](#error_codes)

---

<a name="stack-details"></a>Stack Details
-------------

`Python 3.7.2` + `Django 2.2.4` + `mysql Ver 14.14 Distrib 5.7.25`

See requirements.txt for all lib/module/apps required

Note: There are multiple way to maintain python virtual environemnt
here we using `pydev`
See https://realpython.com/intro-to-pyenv/ 

<a name="dev-setup"></a>Development Setup
-------------

*Create Virtual environement:*

	$ pyenv virtualenv <python_version> <environment_name>
  $ pyenv local myproject
  $ pyenv local system # To deactivate the current and switch to default shell

**Install dependencies:**

    $ pip install -r requirements.txt

**Prepare**

*Create Mysql database name `se_archive`*

*Update your local mysql config in `mysql.cnf`*

*Run Migration, this will create all required tables:*
    
    $ ./manage.py migrate

*Load Initial Data:*

    $ ./manage.py loaddata archive/fixtures/initial.json
  
*Run the server server*
  
   `$ ./manage.py runserver`
   
*Server should be running on `http://127.0.0.1:8000/`*

*Admin can be accessed from `http://127.0.0.1:8000/admin`*
```
username - admin
password - password
```

<a name="api-documentation"></a> API Documentation
=============

### End points

# to-do

---

<a name="error_codes"></a>Error Codes
-------------

**Error codes:**

# to-do

---

