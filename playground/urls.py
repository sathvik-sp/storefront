from django.urls import path
from . import views

#urlConfig
urlpatterns = [
    path('',views.sayHello),
    path('add/',views.add),
]