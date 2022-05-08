from cmath import log
from django.urls import path, include
from django.contrib.auth import views as av
from . import views

urlpatterns = [
    #path('login/',views.user_login, name='login'),
    path('login/', av.LoginView.as_view(),name='login'),
    path("logout/", av.LogoutView.as_view(), name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
      # change password urls
   path('password_change/',
        av.PasswordChangeView.as_view(),
        name='password_change'),
   path('password_change/done/',
         av.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
         # reset password urls
   path('password_reset/',
        av.PasswordResetView.as_view(),
        name='password_reset'),
   path('password_reset/done/',
        av.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
   path('reset/<uidb64>/<token>/',
        av.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
   path('reset/done/',
        av.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
     path('',include('django.contrib.auth.urls')),
     path('register/', views.register, name='register'),
     path('edit/', views.edit, name='edit'),
 

     
]
