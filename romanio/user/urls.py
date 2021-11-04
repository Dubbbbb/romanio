from django.urls import path
from .views import *
from django.conf.urls import url
from django.contrib.auth.views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls.conf import include
# from django.conf import settings
# from django.contrib.auth.views import logout


urlpatterns = [
    path('signin/', UserSignIn.as_view(), name="signin"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    path('', include('social_django.urls', namespace='social')),
    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
    # name='logout'),
    # http://127.0.0.1:8000/auth/authorized/complete/google-oauth2/
    

    url(r'^password-reset/$', PasswordResetView.as_view(
        template_name='user/password_reset_form.html',
        subject_template_name = 'user/title_email.txt',
        html_email_template_name = 'user/password_reset_email.html',
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
