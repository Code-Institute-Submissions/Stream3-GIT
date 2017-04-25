from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from account.forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from blog.models import Post
from django.utils import timezone
import datetime
import stripe


stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
def get_index(request):
    pagetitle = "Tasty Times"
    subtitle = "Enjoy it."
    # now return the rendered template
    return render(request, 'index.html', {'pagetitle':pagetitle, 'subtitle':subtitle})

def profile(request):
    pagetitle = "Profile Page"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'profile.html', {'pagetitle': pagetitle, 'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
 
            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
 
            else:
                messages.error(request, "unable to log you in at this time!")
 
    else:
        form = UserRegistrationForm()
    pagetitle = "Register"
    subtitle = "Enter your data to enjoy our webpage."
    args = {'form': form, 'pagetitle': pagetitle, 'subtitle': subtitle}
    args.update(csrf(request))
    return render(request, 'register.html', args)

def login(request):
    pagetitle="Login"
    subtitle="Enter your data"
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))
 
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
 
    else:
        form = UserLoginForm()
 
    args = {'form':form, 'pagetitle': pagetitle, 'subtitle': subtitle}
    args.update(csrf(request))
    return render(request, 'login.html', args)

@login_required(login_url='/login/')
def profile(request):
    pagetitle = "Profile Page"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'profile.html', {'pagetitle': pagetitle, 'posts': posts})

def logout(request):
    pagetitle = "Tasty Times"
    subtitle = "Logout"
    args = {'pagetitle': pagetitle, 'subtitle': subtitle}
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html', args)

