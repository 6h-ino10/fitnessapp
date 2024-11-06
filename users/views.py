from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView,TemplateView
from .forms import LoginForm,SignupForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.

class LoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self,form):
        response = super().form_valid(form)

        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)

        return response
    
class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('signup_complete')

    def form_valid(self, form):
        #print("form_valid executed")
        #if form.is_valid():
        form.save()
        return redirect('signup_complete')
        #else:
        #    print(form.errors)
        #    return self.form_invalid(form)
        
    def form_invalid(self,form):
        print("form_invalid executed")
        print(form.errors)
        return super().form_invalid(form)
    
class SignupCompleteView(TemplateView):
    template_name = 'signup_complete.html'
        
