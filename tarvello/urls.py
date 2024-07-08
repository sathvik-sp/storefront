from django.urls import path
from . import views

#urlConfig
urlpatterns = [
    path('',views.index,name="index"),
]