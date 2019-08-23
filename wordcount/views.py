from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'Home.html')

def count(request):
    text = request.GET['text']

    words = text.split()

    worddictionary = {}

    for word in words:
        if word in worddictionary:
            #increase count
            worddictionary[word] += 1
        else:
            #add word
            worddictionary[word] = 1    

    Swords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'text':text, 'count':len(words), 'wordD':Swords})

def about(request):
    return render(request, 'about.html')