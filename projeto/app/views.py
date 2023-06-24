from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from app.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from app.models import InfoPlus
from app.forms import UserEditForm, InfoPlusEditForm

# Create your views here.
class LoginView(TemplateView):
    template_name = 'pages-login.html'
    login_form = AuthenticationForm()

    def get_context_data(self):
        return {
            'login_form': self.login_form,
        }

    def post(self, request): 
        self.login_form = AuthenticationForm(data=request.POST)
        if self.login_form.is_valid():
            user = self.login_form.get_user()
            login(request, user)
            if not getattr(user, 'info_plus', False):
                InfoPlus.objects.create(user=user)
            return redirect('dashbord')
        return render(request, self.template_name, self.get_context_data())


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')


class MyProfile(LoginRequiredMixin, View):
    template_name = 'users-profile.html'
    
    def get_context_data(self):
        return {
            'user_form': self.user_form,
            'info_plus_form': self.info_plus_form,
        }

    def get(self, request): 
        self.user_form = UserEditForm(instance=request.user)
        self.info_plus_form = InfoPlusEditForm(instance=request.user.info_plus)
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request): 
        self.user_form = UserEditForm(request.POST, instance=request.user)
        self.info_plus_form = InfoPlusEditForm(request.POST, request.FILES, instance=request.user.info_plus)
        print(request.FILES)
        if self.user_form.is_valid():
            self.user_form.save()
        if self.info_plus_form.is_valid():
            user_info_plus = self.info_plus_form.save(commit=False)
            user_info_plus.user = request.user
            user_info_plus.save()
        return render(request, self.template_name, self.get_context_data())


class DashBordView(LoginRequiredMixin, TemplateView):
    template_name = 'charts-apexcharts.html'
    

    
