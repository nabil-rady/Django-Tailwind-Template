from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forms', views.forms, name='forms'),
    path('cards', views.cards, name='cards'),
    path('charts', views.charts, name='charts'),
    path('buttons', views.buttons, name='buttons'),
    path('modals', views.modals, name='modals'),
    path('tables', views.tables, name='tables'),
    path('login', views.login, name='login'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('create_account', views.create_account, name='create_account'),
    path('blank', views.blank, name='blank'),
    path('404', views.template404, name='template404'),
]
