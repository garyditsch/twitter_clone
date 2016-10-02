from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TweetMessage, Profile, Promo
from .forms import TweetMessageForm, UserRegistrationForm, ProfileForm, PromoForm
from twilio.twiml import Response
from django_twilio.decorators import twilio_view


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
        form3 = PromoForm(request.POST)

        if form.is_valid() and form3.is_valid():
            codes = Promo.objects.all()
            user_code = form3.save(commit=False)
            for code in codes:
                if user_code.promo_code == code.promo_code: 
                    new_user = form.save(commit=False)
                    new_user.set_password(form.cleaned_data['password'])
                    # new_user.promo_code = user_code.promo_code
                    new_user.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                            )
            login(request, new_user)
            messages.success(request, "User Created!")

            return redirect('tweet_messages:user_list')
    else:
        form = UserRegistrationForm()
        form3 = PromoForm()

    context = {
        "form": form,
        "form3": form3,
    }
    return render(request, "tweet_messages/registration.html", context)

@twilio_view
def reply_to_sms_messages(request):
    # import pdb; pdb.set_trace()
    r = Response()
    r.message('Stupid Twilio!')
    return r