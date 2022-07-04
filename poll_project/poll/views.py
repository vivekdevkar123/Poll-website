from django.shortcuts import render,redirect

from .forms import CreatePollForm
from .models import Poll

# Create your views here.

def index(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request,'index.html',context)


def addpoll(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request,'create.html',context)

def vote(request):
    context = {

    }
    return render(request,'vote.html',context)



def result(request,poll_id):
    poll = Poll.objects.get(pk = poll_id)
    context = {
        'poll' : poll
    }
    return render(request,'result.html',context)



def register(request):
    context = {

    }
    return render(request,'register.html',context)



def login(request):
    context = {

    }
    return render(request,'login.html',context)



def profile(request):
    context = {

    }
    return render(request,'profile.html',context)



def logout(request):
    context = {

    }
    return render(request,'index.html',context)