from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser, CustomGroup, UserRole


# TODO: add comments

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class InfoUserForm(forms.ModelForm):
    name = forms.CharField(min_length=3, max_length=64)
    surname = forms.CharField(min_length=3, max_length=64)

    class Meta:
        model = CustomUser
        fields = ('name', 'surname', 'birthday_at')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class UserRoleForm(forms.ModelForm):
    # Define the user and group fields as dropdown menus with all available options
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    group = forms.ModelChoiceField(queryset=CustomGroup.objects.all())

    class Meta:
        model = UserRole
        fields = ('user', 'group')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'surname', 'birthday_at')
