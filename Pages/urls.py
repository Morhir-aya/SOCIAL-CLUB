from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('logout_user',views.logout_user, name='logout'),
    path('inscription/',views.inscription,name='inscription'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('actualite/',views.actualite,name='actualite'),
    path('reservation/',views.reservation,name='reservation'),
    path('reservation1/',views.reservation1,name='reservation1'),
    path('reservation2/',views.reservation2,name='reservation2'),

    #########################################
    path('actualite2/',views.actualite2,name='actualite2'),
    path('admin1/',views.admin1,name='admin1'),
    path('more1/',views.more1,name='more1'),
    path('more2/',views.more2,name='more2'),
    path('post/',views.post,name='post'),

]