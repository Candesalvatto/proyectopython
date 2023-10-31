from django import forms 

class FormularioRegistrar(forms.Form):         #formulario para class Cliente del models
    nombre = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    contrasena= forms.IntegerField(label="", required=True, widget=forms.NumberInput(attrs={'placeholder': 'Contraseña'}))
    

class FormularioLoguin(forms.Form):
    email = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    contrasena= forms.IntegerField(label="", required=True, widget=forms.NumberInput(attrs={'placeholder': 'Contraseña'}))
