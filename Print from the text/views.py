# Created by Lohith
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def about(request):

    import os
    file_path =os.path.join(os.getcwd(), "big_data.txt")
    with open(file_path) as f:
        op = f.read()
    return HttpResponse(op)

