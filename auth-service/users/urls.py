from django.urls import path
from .views import RegisterView, LoginView, VerifyTokenView
from auth_service.constants import ViewsUrls, ViewsNames

urlpatterns = [
    path(ViewsUrls.REGISTER.value, RegisterView.as_view(), name=ViewsNames.REGISTER.value),
    path(ViewsUrls.LOGIN.value, LoginView.as_view(), name=ViewsNames.LOGIN.value),
    path(ViewsUrls.VERIFY_TOKEN.value, VerifyTokenView.as_view(), name=ViewsNames.VERIFY_TOKEN.value),
]
