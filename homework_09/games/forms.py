from django import forms
from .models import Game,RentGame

class GameForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        initial='New Game',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Game Name',
                   'class': 'form-control'}
            )
    )
    class Meta:
        model = Game
        fields = '__all__'


class RentForm(forms.ModelForm):
    name = forms.CharField(
        label='Rent',
        initial='Rent Game',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Game Name',
                   'class': 'form-control'}
            )
    )
    rent = forms.ModelMultipleChoiceField(
        queryset = Game.objects.all(),
        required = False,
        widget = forms.CheckboxSelectMultiple(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = RentGame
        fields = '__all__'