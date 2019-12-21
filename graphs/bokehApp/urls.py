from django.urls import path
from .import views

urlpatterns=[
    path("",views.home, name="home"),
    path("starter/",views.starter, name="Starter"),
    path("learning_graph/",views.learning_graph, name="Learning")
]