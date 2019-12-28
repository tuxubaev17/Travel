from django import forms
from cities.models import City


class RouteForm(forms.Form):

    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}
    ))

    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}
    ))

    across_cities = forms.ModelMultipleChoiceField(label='Через города', required=False, queryset=City.objects.all(),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'class': 'form-control js-example-basic-multiple'}
                                                   ))

    travelling_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'placeholder': 'Время в пути'}
    ))
