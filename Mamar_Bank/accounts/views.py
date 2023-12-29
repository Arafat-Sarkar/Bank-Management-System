from django.shortcuts import render,redirect
from django.views.generic import FormView,UpdateView
from .forms import UserRegistrionForm ,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

# Create your views here.
class UserRegistrtionView(FormView):
    template_name = 'accounts/user_registraton.html'
    form_class = UserRegistrionForm
    success_url = reverse_lazy('register')
    def form_valid(self, form):
        user = form.save()
        login( self.request, user)
        return super().form_valid(form) #form_valid function ta call hobe jodi shob thik thekhe
    
class UserLoginView(LoginView):
    template_name = 'accounts/User_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_sucess_url(self):
            if self.request.user.is_authenticated:
                logout(self.request)
            return reverse_lazy('home')
        
class UserUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})