from django.shortcuts import render
from django.http import  HttpResponse
from .forms import Post_form, Email_Form

# Create your views here.
def index(request):
    return HttpResponse('hello')

def add_post(request):
    f = Post_form()
    content = {'form': f}
    return render(request, 'news/add_news.html',content)

def save_news(request):
    if request.method == 'POST':
        p = Post_form(request.POST)
        if p.is_valid():
            p.save()
            return HttpResponse('save post')
        else:
            return HttpResponse('is not valid')
    else:
        return HttpResponse('is not POST request')

def emailView(request):
    form = Email_Form()
    content = {'form': form}
    return render(request, 'news/Send_Email.html', content)

def process(request):
    if request.method == 'POST':
        m = Email_Form(request.POST)
        if m.is_valid():
            title = m.cleaned_data['title']
            content = m.cleaned_data['content']
            email = m.cleaned_data['email']
            cc = m.cleaned_data['cc']
            context = {'title':title,'content':content,'email':email, 'cc':cc}
            return render(request, 'news/detail_email.html',context)
        else:
            return HttpResponse('is not valid')
    else:
        return  HttpResponse('is not post method')

