from django.db import models
# from django.core.urlresolvers import reverse

# Create your models here.
"""
class Player(models.Model):
  player = models.CharField(max_length=15)
  letter = models.CharField(max_length=1)
  value = models.IntegerField()

class Board(models.Model):
  row = models.IntegerField()
  col = models.IntegerField()
"""

class Game(models.Model):
  player1 = {
    "letter" = "X",
    "value" = 1
  }
  player2 = {
    "letter" = "O",
    "value" = -1
  }

  board = {}
  def new_board(): # for starting and restarting the game
    board = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
      7: 0,
      8: 0,
      9: 0
    }

  def check_for_winners():
    if abs(board[1] + board[5] + board[9]) == 3:
      return true
    elif abs(board[1] + board[4] + board[7]) == 3:
      return true
    elif abs(board[1] + board[2] + board[3]) == 3:
      return true
    elif abs(board[4] + board[5] + board[6]) == 3:
      return true
    elif abs(board[7] + board[8] + board[9]) == 3:
      return true
    elif abs(board[2] + board[5] + board[8]) == 3:
      return true
    elif abs(board[3] + board[5] + board[7]) == 3:
      return true
    elif abs(board[3] + board[6] + board[9]) == 3:
      return true
    else return false

  def player_turn(turn):
    if turn % 2 == 0
      player = "Player 1"
      letter = player1.letter
      value = player1.value
    else
      player = "Player 2"
      letter = player2.letter
      value = player2.value

  def move(board_position): # will come from the UI
    turn = 0
    for turn in board.length():
      board[board_position] = player_turn().value
      if check_for_winners() == true:
        return player_turn(turn).player
      turn ++
