from django.urls import path
from . import  views
app_name = 'news'
urlpatterns = [
    path('',views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('save_news/',views.save_news, name='save_news'),
    path('send_email/', views.emailView, name='send_email'),
    path('process/', views.process, name='process'),

]