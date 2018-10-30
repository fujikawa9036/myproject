from django.urls import path

from . import views

urlpatterns = [
    path('', views.SampleTemplateView.as_view(), name='index'),
]