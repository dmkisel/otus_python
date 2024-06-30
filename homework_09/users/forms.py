from django.contrib.auth.forms import UserCreationForm


from .models import AppUser

class RegisretForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'name','phone', 'telegram', 'address', 'password1', 'password2')







