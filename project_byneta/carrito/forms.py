from django import forms 
from carrito.models import Carrito

class FormularioCarrito(forms.Form):         #formulario para class Cliente del models
    producto = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Producto'}))
    cantidad = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}))
    precio= forms.IntegerField(label="", required=True, widget=forms.NumberInput(attrs={'placeholder': 'Precio'}))

    class Meta:
        model = Carrito
        fields = ['usuario', 'producto', 'precio', 'cantidad', 'imagen']
    
class BuscarProductoCarrito(forms.Form):
    producto = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Buscar Producto'}))

    
    class Meta:
        model = Carrito
        fields = [ 'producto']
    
