from django.conf.urls import url
from . import views
from .forms import LoginForm


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/list$', views.users_list, name='user_list'),
    url(r'^users/(?P<id>\d+)/$', views.user_page, name='user_page'),
    url(r'^users/create-message.html/$', views.create_message, name='create_message'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'authentication_form': LoginForm},
        name='login'),

    url(r'^logout/$', 
        'django.contrib.auth.views.logout', 
        {'template_name': 'registration/logout.html'},
        name='logout'),
    # url(r'^artist/(?P<id>\d+)/$', views.artist_page, name='artist_page'),

]