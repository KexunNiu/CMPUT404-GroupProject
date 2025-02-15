from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from authors.models import single_author,Followers
from django.urls import reverse
from .forms import SignUpForm
from .forms import LoginForm
from .forms import newUserForm
from django.contrib.auth.models import User

import uuid
# Create your views here.
def log_in(request):
    #login by username and password
    displayConfirmMsg = False
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']

        try:
            userLogin = User.objects.get(username = username)
        except:
            return HttpResponse("Username does not exist")

        if userLogin.is_active == False:
            displayConfirmMsg = True
            return render(request,"login/login.html",{
                "form":form,
                "display":displayConfirmMsg
                }) 


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            current_user = request.user
            current_authorId = single_author.objects.get(username=current_user).uuid
            
            return HttpResponseRedirect(reverse("home-page",args=[current_authorId]))
        else:
            return render(request,"login/login.html",{
                "username":None,
                "password":None,
                "form":form,
                "display":displayConfirmMsg
    
            })
        # if single_author.objects.filter(username=username).exists():
        #     password = request.POST.get('password')
        #     storedUser = single_author.objects.get(username=username)
        #     storedUserPassword = storedUser.password
        #     userId = storedUser.id
        #     # if storedUserPassword == password:
        #     #     #redirect this for now
        #     #     # return HttpResponseRedirect("post/index.html",{
        #     #     #     'username':storedUser
        #     #     # })
        #     #     # return HttpResponseRedirect("")
        #     #     return HttpResponseRedirect(reverse("home-page",args=[userId]))
        #     # else:
        #     #     form = LoginForm()
        #     #     isNotPasswordMatch = True
        #     #     return render(request, 'login/login.html',{
        #     #         "form":form,
        #     #         'isNotPasswordMatch':isNotPasswordMatch
        #     #     })
        # else:
        #     form = LoginForm()
        #     isNotUsernameExist = True
        #     return render(request, 'login/login.html',{
        #         "form":form,
        #         'isNotUsernameExist':isNotUsernameExist
        #     })
    else:
        form = LoginForm()

    return render(request,"login/login.html",{
        "form":form,
        "display":displayConfirmMsg
    })

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        userForm = newUserForm(request.POST)
        if form.is_valid() and userForm.is_valid():
            new_author = form.save(commit=False)
            # generate something
            authorHost = request.META.get('HTTP_HOST')
            authorId = f"{request.build_absolute_uri('/')}authors/{new_author.uuid}"
            authorUrl = f"{request.build_absolute_uri('/')}authors/{new_author.uuid}"
            new_user = userForm.save(commit=False)
            #### Needs Admin Permission to activate this new account ####
            new_user.is_active = False
            
            #######################
            new_author.username = userForm.cleaned_data['username']
            new_author.password = userForm.cleaned_data['password1']
            new_author.id = authorId
            new_author.host = authorHost
            new_author.url = authorUrl
            new_author.save()
            new_user.save()
            #######################
            
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUpForm()
        userForm = newUserForm()

    return render(request,"login/signup.html",{
        'form':form,
        'newUser':userForm
    })





