from django.urls import path
from accounts.views import (login,reset_password,
                            forget_password, change_password,
                            register, userprofile,logout,
                                                        MyPasswordResetView,
                                                        MyPasswordResetDoneView,
                                                        MyPasswordResetConfirmView,
                                                        MyPasswordResetCompleteView)

from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)



urlpatterns = [
    path('login/', login, name = 'login'),
    path('change_password/', change_password, name = 'change_password'),
    path('reset_password/', reset_password, name = 'reset_password'),
    path('forget_password/',forget_password, name = 'forget_password'),
    path('register/', register , name = 'register'),
    path('user-profile/', userprofile , name = 'userprofile'),
    path('logout/', logout, name= 'logout'),
    path('password_reset/', MyPasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', MyPasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', MyPasswordResetCompleteView.as_view(), name = 'password_reset_complete')

]