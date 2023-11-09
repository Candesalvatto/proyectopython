from django import forms 
from .models import ProductoAccesorios

# class FormularioAccesorios(forms.Form):         #formulario para class Cliente del models
#     nombre = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre del Producto'}))
#     descripcion = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Descripcion'}))
#     precio= forms.DecimalField(label="", max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'placeholder': 'Precio'}))
#     imagen = forms.ImageField(label="Imagen", required=False)

# forms.py



class FormularioAccesorios(forms.ModelForm):
    class Meta:
        model = ProductoAccesorios
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
    
class FormularioAutobronceantes(forms.ModelForm):
    class Meta:
        model = ProductoAccesorios
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
        
class FormularioBrumas(forms.ModelForm):
    class Meta:
        model = ProductoAccesorios
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
