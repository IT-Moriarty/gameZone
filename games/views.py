from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404
from .models import Game, Review

def home(request):
    popular_games = Game.objects.order_by('-rating')[:5]
    return render(request, 'games/home.html', {'popular_games': popular_games})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.all()
    return render(request, 'games/game_detail.html', {'game': game, 'reviews': reviews})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'games/review_list.html', {'reviews': reviews})

def contact(request):
    return render(request, 'games/contact.html')
