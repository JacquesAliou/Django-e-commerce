from django import forms
from django.contrib.auth import authenticate, get_user_model

# tests validation ==> funct stengthen password validation security
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Votre Nom: ")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe: ")

    # to be sure that the data passed in is what we really needed
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # checking if everything matches: if not raise error
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("L'utilisateur n'existe pas")
            if not user.check_password(password):
                raise forms.ValidationError("Le mot de passe est incorrect")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Votre Nom: ")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe: ")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmer le Mot de passe: ")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
        # clean form(without django subtext in form fields)
        help_texts = {
            'username': None,
            'email': None,
            'password': None,
            'password2': None,
        }

    # Form validation
    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')
        if password and password2:
            if password != password2:
                raise forms.ValidationError("Les mots de passe ne correspondent pas")

            # check for email duplicity
            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError("cet email est déjà attribué. Pour continuer, veuillez entrer un nouvel email")

        return super(UserRegisterForm, self).clean(*args, **kwargs)


    # stengthen password validation security




