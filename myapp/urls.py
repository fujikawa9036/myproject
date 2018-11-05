from django.urls import path

from . import views

urlpatterns = [
    path('', views.SampleTemplateView.as_view(), name='index'),
    path('about/',views.About.as_view(), name='about'),
    path('course/',views.Course.as_view(), name='course'),
    path('contact/',views.Contact.as_view(), name='contact'),
    


]