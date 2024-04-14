

# Create your views here.
# game/views.py

from django.shortcuts import render
import random
import os

def home(request):
    return render(request, 'game/home.html')

def play(request):
    choices = ['Stone', 'Paper', 'Scissors']
    user_choice = request.POST.get('choice')
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (user_choice == 'Stone' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Stone') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = 'You win!'
    else:
        result = 'Computer wins!'

    return render(request, 'game/play.html', {'user_choice': user_choice,
                                               'computer_choice': computer_choice,
                                               'result': result})
