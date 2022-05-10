from django.forms import ModelForm
from print4you.models import Printout


class PrintoutForm(ModelForm):
    class Meta:
        model = Printout
        fields = ['is_color', 'is_gloss', 'quantity', 'size', 'image_file']
        labels = {
            'is_color': ('Kolor'),
            'is_gloss': ('Połysk'),
            'quantity': ('Ilość'),
            'size': ('Format'),
            'image_file': ('Plik graficzny')
        }
