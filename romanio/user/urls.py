from django.urls import path, re_path
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView



urlpatterns = [
    path('signin/', UserSignIn.as_view(), name="signin"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    
    path('password-reset/', 
        PassResView.as_view(template_name='user/password_reset_form.html',
        html_email_template_name='user/password_reset_email.html',),
        name='password_reset'),
    
    path('password-reset/done/',
        PasswordResetDoneView.as_view(template_name='user/password_reset_done.html',), 
        name='password_reset_done'),
    
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',), 
        name='password_reset_confirm'),
    
    path('password-reset/complete/',
        PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name='password_reset_complete'),

]
