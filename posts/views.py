from django.shortcuts import render , HttpResponse
import random

def test_view(request):
    return HttpResponse(f"Hello Country{random.randint(1,100)}")



def html_view(request):
    return render(request,'main.html')
def text_response_view(request):
    return HttpResponse("Это текстовый ответ")
def html_template_view(request):
    return render(request, 'myapp/template.html')

