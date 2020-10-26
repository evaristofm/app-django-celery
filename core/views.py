from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

"""
def usersList(request):
    users = User.objects.all()

    context = {'users': users}
    return render(request, 'core/users_list.html', context)
"""
class HomePageView(TemplateView):
    template_name = "core/users_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context



class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')



