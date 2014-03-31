from django.shortcuts import render, get_object_or_404
from tic_tac_toe.models import Game


# Create your views here.
  def index(request):
    player = Player.objects()
    board = Board.objects()
    return render(request, 'tic_tac_toe/index.html', {'game': game})
