from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import CreatePollForm
from .models import Poll

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

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

def vote(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('result', poll.id)

    context = {
        'poll' : poll
    }
    return render(request,'vote.html',context)



def result(request,poll_id):
    poll = Poll.objects.get(pk = poll_id)
    context = {
        'poll' : poll
    }
    return render(request,'result.html',context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account is created for ' + user)
            return redirect('login')

    context = {'form' : form}
    return render(request,'register.html',context)



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            messages.info(request,'username or password is incorrect...')

    context = {

    }
    return render(request,'login.html',context)



def profile(request):
    context = {

    }
    return render(request,'profile.html',context)



def logoutUser(request):
    logout(request)
    return redirect('login')
