from django.contrib import admin

# Register your models here.

from .models import TweetMessage, Profile, Promo


class TweetMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet_messages', 'date', )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bio',)


admin.site.register(TweetMessage, TweetMessageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Promo)
