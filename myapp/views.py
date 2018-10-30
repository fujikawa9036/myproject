from django.views.generic import TemplateView

class SampleTemplateView(TemplateView):
    template_name = "myapp/index.html"