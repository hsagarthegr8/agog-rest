from django.urls import path

from .views import UserList, VerificationList

urlpatterns = [
    path('users', UserList.as_view()),
    path('verifications', VerificationList.as_view())
]