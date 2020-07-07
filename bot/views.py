from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .model import *
bot = Bot()

def respond(request):
    return render(request, 'botpage.html')

@csrf_exempt
def getResponse(request):
    msg = request.POST['msg']
    reponse = bot(msg)
    return JsonResponse({'response': reponse})

