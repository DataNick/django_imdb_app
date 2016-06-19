from django.db import models
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
import json

# Create your models here.

class Movie(models.Model):

  @classmethod
  def getMovieData(cls, title):
    title = urllib.parse.quote(title)
    request = urlopen("http://www.omdbapi.com/?t=%s&y=&plot=short&r=json" % title)
    response = request.read().decode("utf-8")
    data = json.loads(response)

    cls.movieData = {}
    if (data['Response'] == 'True'):
      cls.movieData['Title'] = data['Title']
      cls.movieData['Actors'] = data['Actors'].split(' , ')
      cls.movieData['Language'] = data['Language'].split(' , ')
      cls.movieData['Rated'] = data['Rated']
      cls.movieData['Released'] = data['Released']
      cls.movieData['Plot'] = data['Plot']
      cls.movieData['Writer'] = data['Writer'].split(' , ')
      cls.movieData['Director'] = data['Director']
      cls.movieData['Runtime'] = data['Runtime']
      cls.movieData['Poster'] = data['Poster']
    else:
      cls.movieData['Error'] = data['Error']

    return cls.movieData








