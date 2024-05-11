#i have created this file-riddhi
from django.http import HttpResponse
from django.shortcuts import render
import string
#code for video7
def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext=request.POST.get("text",'default')
    removepunc=request.POST.get("removepunc",'default')
    makecap=request.POST.get("makecap",'default')
    
    analyzed_text=""
    if removepunc=="on" and makecap=="on":
        st=""
        for char in djtext:
            if char not in string.punctuation:
                st=st+char
        for char in st:
            analyzed_text=analyzed_text+char.upper()

    elif removepunc=="on":
        for char in djtext:
            if char not in string.punctuation:
                analyzed_text=analyzed_text+char

    elif makecap=="on":
        for char in djtext:
            analyzed_text=analyzed_text+char.upper()

    else:
        return HttpResponse("error")
    
    params={'purpose':'removed punctuations','analyzed_text':analyzed_text}
    return render(request,'analyze.html',params)

    #analyze the text
    return HttpResponse("rempunc <a href='/'>back</a>")

#views only return http response