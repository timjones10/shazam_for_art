from django.http import HttpResponse
from django.shortcuts import render
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from sklearn.externals import joblib
from skimage import io
from skimage.transform import resize

def images(request):
    return render(request, 'image_uploader/images.html')

def new(request):
    default_storage.delete('tmp/image_to_test.jpg')
    painting = request.FILES['painting']
    image_relative_filepath = default_storage.save('tmp/image_to_test.jpg', ContentFile(painting.read()))
    image_absolute_filepath = os.path.join(settings.MEDIA_ROOT, image_relative_filepath)
    predicted_artist_name = make_prediction(image_absolute_filepath)
    predicted_movement = get_movement(image_absolute_filepath)
    return render(request, 'image_uploader/success.html', {'name': predicted_artist_name, 'movement': predicted_movement})


def make_prediction(image_absolute_filepath):
    ARTISTS = ["Constable", "Hopper", "Kandinsky" ,"Lowry", "Monet", "Rembrandt", "Rothko", "Rubens", "Turner", "Van Gogh"]
    painting_data = io.imread(image_absolute_filepath)
    clf = joblib.load(os.path.join(settings.MEDIA_ROOT, 'svm_flatten_pixels_v3.pkl'))
    resized_painting = resize(painting_data, (200, 200))
    painting_flattened = []
    for row in resized_painting:
        for pixel in row:
            for colour in pixel:
                painting_flattened.append(colour)
    result = clf.predict([painting_flattened])
    return ARTISTS[result[0]]

def get_movement(image_absolute_filepath):
    MOVEMENTS = ['Expressionistic cubism',
                 'Romantic colour fields',
                 'Impressionistic cloisonnism',
                 'Expressionistic colour fields',
                 'Cloisonnism-cubism',
                 'Baroque colour fields',
                 'Cloisonnistic colour fields',
                 'Expressionistic-cloisonnistic colour fields',
                 'Orangey-red colour fields',
                 'Paler colour fields'
                 ]
    GRID_WIDTH = 20
    painting_data = io.imread(image_absolute_filepath)
    clf = joblib.load(os.path.join(settings.MEDIA_ROOT, 'unsupervised.pkl'))
    resized_painting = resize(painting_data, (200, 200))
    result = []
    for i in range(10):
        for j in range(10):
            grid = resized_painting[
                i*GRID_WIDTH:i*GRID_WIDTH+GRID_WIDTH,
                j*GRID_WIDTH:j*GRID_WIDTH+GRID_WIDTH,
                :
            ]
            result.append(grid[:, :, 0].mean())
            result.append(grid[:, :, 1].mean())
            result.append(grid[:, :, 2].mean())
    result = clf.predict([result])
    return MOVEMENTS[result[0]]
