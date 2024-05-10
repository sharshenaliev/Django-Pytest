from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from account.models import MyUser


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = "__all__"


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = '__all__'


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    ordering = ('email',)
    list_display = ('id', 'email',)
    list_display_links = ('email',)
    list_filter = ('is_staff', )
    readonly_fields = ("last_login",)
    fieldsets = ((None, {'fields': ('email', 'password', 'first_name', 'last_name', 'last_login')}),
                 (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'groups')}))
    add_fieldsets = (
        (None, {"fields": ('email', 'first_name', 'last_name',
                           'password1', 'password2', 'is_staff', 'is_superuser', 'groups')}),
    )
