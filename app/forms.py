from django import forms
from .models import CardClassification
from .models import Card


class CardSearchForm(forms.Form):
    company = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    classification = forms.ModelChoiceField(CardClassification.objects, label='Class', required=False)


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'


class CardImageAddForm(forms.Form):
    image = forms.FileField(label='image')
