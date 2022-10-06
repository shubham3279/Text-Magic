# I have created this file  - Shubham

from email.policy import default
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):

    the_text = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremove_option = request.GET.get('newlineremove','off')

    
    if removepunc == 'on':
        punctuations = '''!()-{}[];:'"|\?/>.<,~`@#$%^&*_+='''
        analyzed = ""
        for char in the_text:
            if char not in punctuations:
                analyzed = analyzed + char 

        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif fullcaps == 'on' :
        analyzed = ""
        for char in the_text:
            analyzed = analyzed + char.upper()

        params = {'purpose':'FULL CAPITALIZED TEXT', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)


    elif newlineremove_option == 'on':
        analyzed = ""
        for char in the_text:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse('Error.')



        


