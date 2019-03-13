[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4fea0f7323a24b7487c1660cd40add8e)](https://app.codacy.com/app/larryTheGeek/EbookManager?utm_source=github.com&utm_medium=referral&utm_content=larryTheGeek/EbookManager&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/larryTheGeek/EbookManager.svg?branch=develop)](https://travis-ci.com/larryTheGeek/EbookManager)
[![Coverage Status](https://coveralls.io/repos/github/larryTheGeek/EbookManager/badge.svg)](https://coveralls.io/github/larryTheGeek/EbookManager)

# EbookManager
Ebookmanager is a platform that keeps a record of books available in a book shop.

### Framework used
The application is built using python: Django Rest framework.
>[Django Rest](https://www.django-rest-framework.org/topics/documenting-your-api/)
### End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/auth/signup` |  Register a user. |
|POST| `api/v1/auth/login` | Login user.|
|POST| `api/v1/books` | Share a book. |
|GET| `api/v1/books` | Get all all books. |
|GET| `api/v1/books/user` | Get all the books created by the current user who is logged in. |
|GET| `api/v1/books/<book_id>` | Get a single book. |
|PUT| `api/v1/books/<book_id>/title` | Update a book title. |
|DELETE| `api/v1/books/<book_id>` | Delete a book incident. | 

## Installation 🕵
- To run on local machine git clone this project :
```
$ git clone https://github.com/larryTheGeek/EbookShare.git
```
Copy and paste the above command in your terminal, the project will be downloaded to your local machine.

To Install python checkout:
```
https://www.python.org/
```

- create a virtualenv and make it use python 3 using the following command.
```

$ pipenv shell
```
- Install Requirements
```
$ pipenv sync
```
### Testing
- Run the following command
```
$ python manage.py test
```

The app can also be tested via Postman
- Run App 
```
$ python manage.py runserver
```
The app should be accessiable via : http://127.0.0.1:8000/

open postman and navigate to the API endpoints described above
