from django.urls import path
from .views import *
from django.conf.urls import url
from django.contrib.auth.views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
    path('signin/', UserSignIn, name="signin"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    url(r'^password-reset/$', PasswordResetView.as_view(
        template_name='user/password_reset_form.html',
    ), name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html',
    ), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html',
    ), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html',
    ), name='password_reset_complete'),

]
