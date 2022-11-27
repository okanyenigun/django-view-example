from django.forms import ModelForm
from home.models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

