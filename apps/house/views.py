from django.shortcuts import render

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'home.html'  # Default template

    # def get_template_names(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         if Customer.objects.filter(pk=user.pk).exists():
    #             return ['customer/home.html']
    #         elif Salesman.objects.filter(pk=user.pk).exists():
    #             return ['salesman/home.html']
    #         elif Staff.objects.filter(pk=user.pk).exists() or user.is_superuser:
    #             return ['home.html']
    #     return [self.template_name]