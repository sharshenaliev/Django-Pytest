from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from account.serializers import TokenSerializer, RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(ObtainAuthToken):
    serializer_class = TokenSerializer


class LogoutView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        queryset = Token.objects.all()
        filter_kwargs = {'user': self.request.user}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
