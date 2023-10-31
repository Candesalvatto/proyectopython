from django import forms 

class FormularioAccesorios(forms.Form):         #formulario para class Cliente del models
    nombre = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre del Producto'}))
    descripcion = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Descripcion'}))
    precio= forms.DecimalField(label="", max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'placeholder': 'Precio'}))
