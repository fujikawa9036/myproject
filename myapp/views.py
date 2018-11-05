from django.views.generic import TemplateView

class SampleTemplateView(TemplateView):
    template_name = "myapp/index.html"

class About(TemplateView):
    template_name = "myapp/about.html"

class Course(TemplateView):
    template_name = "myapp/course.html"

class Contact(TemplateView):
    template_name = "myapp/contact.html"