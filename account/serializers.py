from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from account.models import MyUser


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        exclude = ('favorite', 'last_login', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        user = MyUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_token(self, instance):
        token = Token.objects.create(user=instance)
        return token.key
