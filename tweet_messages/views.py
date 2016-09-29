from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TweetMessage, Profile
from .forms import TweetMessageForm, UserRegistrationForm

def index(request):

    tweets = TweetMessage.objects.all()

    context = {
        "tweets": tweets,
    
    }

    return render(request, "tweet_messages/index.html", context)

def users_list(request):

    user_list = User.objects.all()

    context = {
        "user_list": user_list,
    }

    return render(request, "tweet_messages/user_list.html", context)

def user_page(request, id):
    tweeter = get_object_or_404(User, pk=id)
    tweets = tweeter.tweetmessage_set.all()

    context = {
        "tweets": tweets,
        "tweeter": tweeter,
    }

    return render(request, "tweet_messages/user_page.html", context)

@login_required
def create_message(request):

    if request.method == "POST":
        form = TweetMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_id = request.user.pk
            new_message.save()
            messages.success(request, 'Message Posted!')
            return redirect('tweet_messages:index')
    else:
        form=TweetMessageForm()

    context = {
        "form": form,
    }

    return render(request, "tweet_messages/create_message.html", context)


def register(request):
    if request.method== "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "User Created!")

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return redirect('tweet_messages:user_list')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }
    return render(request, "tweet_messages/registration.html", context)