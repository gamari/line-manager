from django.contrib.auth.views import LoginView

from .forms import LoginForm

class AccountLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    
    # TODO dashboardページに遷移する処理
    