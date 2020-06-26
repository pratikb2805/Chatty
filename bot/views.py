from django.shortcuts import render

from .model import *
bot = Bot()

def respond(request):
    try:
        msg = request.POST['message']
        response = f"{bot.name}:\n" + bot(msg)
        response = {'chats' : [bot.user + ':\n' + msg, response]}
    except:
        response = f"{bot.name}: " + "Hi, I am Chatty!"
        response = {'chats' : [ response]}
    
    return render(request, 'botpage.html', response)