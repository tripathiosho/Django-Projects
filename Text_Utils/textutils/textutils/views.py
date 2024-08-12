from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if fullcaps =='on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':'Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if newlineremover == 'on' :
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed += char
        params = {'purpose':'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if extraspaceremover == 'on':
        analyzed = ""
        length = len(djtext)  
        for index in range(length):
            if djtext[index] == " ":
                if index + 1 < length and djtext[index + 1] == " ":
                    continue  
            analyzed += djtext[index]  
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if charcounter == 'on':
        analyzed = " Total Chacarter in your input are: ->  "+str(len(djtext))
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")