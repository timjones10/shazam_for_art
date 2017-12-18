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

1. Import Libraries
2. Load Dataset
3. Get visualisation on the data

![screen shot 2017-12-05 at 14 15 49](https://user-images.githubusercontent.com/27693622/33612716-62f8bb24-d9ca-11e7-900d-cf429e13afa9.png)

![screen shot 2017-12-05 at 14 15 59](https://user-images.githubusercontent.com/27693622/33612755-8385d26e-d9ca-11e7-95a5-6d8c9dbaf97d.png)


## Tuesday:
We set out to answer these three key questions:
  1. Which feature extraction to do first? HOG, Pixel, Colour Histogram etc
  2. What is the order of the scikit pipeline?
  3. How does classification work?
      - Do we implement 'supervised'
      - Do we implement 'unsupervised'
  4. Imported algorithm from scikit-learn to process an 'unseen' image vs our image bank and return a value. 0 => Lowry, 1 => Turner. Our program successfully assigned the correct value to the unseen image.
  5. MVP reached

## Wednesday:
  We included and compared 3 algorithms to check the artist of a painting. From sklearn we imported DecisionTree, SVM and Neural_Network. The results were as follows:

![screen shot 2017-12-08 at 10 56 07](https://user-images.githubusercontent.com/27693622/33763499-9d63ab94-dc08-11e7-8274-a5e277f8d2b9.png)

At a glance svm_pixels appeared to be the most effective algorithm in terms of predicting the correct artist. This was a big break through as we had achieved 50% accuracy.

## Thursday:
We tested existing code and created an effective TDD with higher test coverage in our analysis branch. We also researched Django using tutorials and began to build our front end website with Django.


## Friday:
We refactored existing code and increased test coverage. We continued with Django progressing into building a simple image upload form


## Monday:
We built a Django web app, complete with testing and began implementing some styling
We continued to refine the machine learning and improve on our rate of probability

## Tuesday:
We set out to complete a few key tasks:
  1. Add the remainig features for the app - iRobArt, art movement, art recommendations based on input
  2. Styling the front end
  3. Connecting the front end with the logic an machine learning
  4. Prepare the presentation - to get started and brainstorm ideas
