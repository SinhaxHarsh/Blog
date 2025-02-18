from django.urls import path
from .views import SignUpView,SignInView,SignOutView

urlpatterns = [
    path('sign-up/',SignUpView,name="signup"),
    path('sign-in/',SignInView,name="signin"),
    path('sign-out/',SignOutView,name="sign-out"),
]
