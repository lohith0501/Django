from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)

    # Check checkbox values
    wordcount = request.GET.get('wordcount', 'off')

    #Check which checkbox is on
    if wordcount == "on":
        txt = djtext.replace(",", " ")
        txt_list = txt.split()

        track = {}
        cnt = 1
        for i in txt_list:
            if i not in track.keys():
                track.update({i: cnt})
            else:
                track[i] += 1

        params = {'purpose': 'Count unique words', 'analyzed_text': track}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")


