from django.urls import path

from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('<str:short_id>', views.go, name='go')

]