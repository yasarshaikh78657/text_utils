#i have created this file yasar
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name':'yasar','place':'india'}
    return render(request,'index.html')

def analyze(request):
    recived_text = request.GET.get('text','default')

    #panctuation part
    recived_removepunc = request.GET.get('removepunc', 'off')
    if recived_removepunc =="on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in recived_text:
            if ele in punc:
                recived_text = recived_text.replace(ele, "")

    #Capitalize First
    recived_capfirst = request.GET.get('capfirst', 'off')
    if recived_capfirst =="on":
        recived_text = recived_text.title()

    #Upper case
    recived_uppercase = request.GET.get('uppercase', 'off')
    if recived_uppercase =="on":
        recived_text = recived_text.upper()

    # lower case
    recived_lowercase = request.GET.get('lowercase', 'off')
    if recived_lowercase  == "on":
        recived_text = recived_text.lower()

    #Newline Remover
    recived_newlineremover = request.GET.get('newlineremover', 'off')
    if recived_newlineremover == "on":
        for ele in recived_text:
            if ele=="\n":
                recived_text = recived_text.replace(ele, "")

    #Space Remover
    recived_spaceremover = request.GET.get('spaceremover', 'off')
    if recived_spaceremover == "on":
        for ele in recived_text:
            if ele == " ":
                recived_text = recived_text.replace(ele, "")

    #Character count
    recived_charcount = request.GET.get('charcount', 'off')
    if recived_charcount == "on":
        n = 0
        for ele in recived_text:
            n = n + 1
        params ={'purpose':'here','analyzed': recived_text + "count =" + str(n)}
    else:
        params ={'analyzed': recived_text}
    return render(request,'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remover")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def char_count(request):
#     return HttpResponse("charater count")