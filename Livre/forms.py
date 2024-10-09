from django.forms import ModelForm, DateTimeInput
from .models import Livre

class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields= '__all__'