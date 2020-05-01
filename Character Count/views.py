# Created by Lohith

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def charcount(request):
    paragraph = request.GET.get('text', 'default')
    char_count = request.GET.get('char_count', 'default')
    if char_count=="on":
        paragraph_split=paragraph.split()
        track = {}
        cnt = 1
        for i in paragraph_split:
            if i not in track.keys():
                track.update({i: cnt})
            else:
                track[i] += 1

    params={"name":track}
    return render(request, 'output.html',params)


