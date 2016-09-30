from django.contrib import admin

# Register your models here.

from .models import TweetMessage, Profile, Promo


class TweetMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet_messages', 'date', )

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(TweetMessage, TweetMessageAdmin)
admin.site.register(Profile)
admin.site.register(Promo)
