from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('accounts/', include('api.accounts.urls'))
]