from django.shortcuts import render
from filmster.models import Movie

# Create your views here.
def index(request):
  return render(request, 'filmster/index.html', {})

def search(request):
  if 'q' in request.GET:
    q = request.GET['q']
    movie = Movie.getMovieData(q)
    return render(request, 'filmster/index.html', {'movie': movie, 'query': q})
  else:
    message = 'You submitted an empty form.'

  # return render(request, 'filmster/index.html', {})