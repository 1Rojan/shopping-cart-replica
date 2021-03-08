from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    form = UserRegisterForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Account created')
            return HttpResponseRedirect('/users/login/')
        else:
            return render(request, 'users/register.html',context)

    else:

        return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated')
            return HttpResponseRedirect('/users/profile/')
    else:
        context = {
            'u_form' : UserRegisterForm( instance= request.user),
            'p_form' : ProfileUpdateForm( instance=request.user.profile)
        }
        return render(request, 'users/profile.html', context)




