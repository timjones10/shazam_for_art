## Artvark - (Shazam for art)

Web application which uses machine learning to identify the artist from a previously unseen image of a painting.

### Getting started

We hosted the web app locally so to get it up and running you will need to:

* Install Python 3
```
brew install python3
brew postinstall python3
```
* Install numpy and scipy
```
pip3 install --user numpy
pip3 install --user scipy
```
* Install Scikit-Learn
```
pip3 install -U scikit-learn
```

* Install Scikit Image
```
pip install -U scikit-image
```
* Install Django
```
pip3 install django
```
Clone this repo and navigate to ./imageuploader/manage.py

Apply the migrations

```
python3 manage.py migrate
```
Run the server

```
python3 manage.py runserver
```

Open your browser and head to http://127.0.0.1:8000/images

Upload an image of a painting and see how it does!

## Built with

[Python3](https://www.python.org/download/releases/3.0/)
[Django](https://www.djangoproject.com/) - Web Framework for Python
[PyTest](https://docs.pytest.org/en/latest/) - Testing Framework
[Scikit Image](http://scikit-image.org/) - Image Processing in Python
[Scikit Learn](http://scikit-learn.org/stable/) - Machine Learning in Python
