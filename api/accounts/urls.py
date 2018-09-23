from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token, verify_jwt_token

from .views import UserList, VerificationList

urlpatterns = [
    path('users', UserList.as_view()),
    path('verifications', VerificationList.as_view()),
    path('get-token', obtain_jwt_token),
    path('refresh-token', refresh_jwt_token),
    path('verify-token', verify_jwt_token)
]
