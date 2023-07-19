from django.urls import path
from .views import index, top_sellers, register, profile, login, advertisement_post, advertisement

urlpatterns = [

    path('', index, name='main-page'),

    path('top-sellers/', top_sellers, name='top-sellers'),

    path('register/', register, name='register'),

    path('profile/', profile, name='profile'),

    path('login/', login, name='login'),

    path('advertisement-post/', advertisement_post, name='advertisement-post'),

    path('advertisement/', advertisement, name='advertisement'),


]