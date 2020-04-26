# Created by Lohith
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello")

def about(request):

    op= '''<h1>Navigation Bar<br></h1>
        <a href="https://www.youtube.com/">Youtube</a><br>
        <a href="https://www.amazon.com/">Amazon</a><br>
        <a href="https://www.udemy.com/">Udemy</a><br>
        <a href="https://www.espncricinfo.com/">Cricinfo</a>'''
    return HttpResponse(op)

