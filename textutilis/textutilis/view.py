# I have created this file - Mustafa
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>Mustafa</h1> <a href="https://www.youtube.com/watch?v=TFO9hBtLVec&ab_channel=AlphaMotivation"> its motivation music</a>''')

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    # check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)

    # Check which checkbox is on
    if removepunc == "on":
        # analyzed = djtext
        punctuations ='''!()-{}[];:'"\,<>.?/@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctutions', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("character count")

