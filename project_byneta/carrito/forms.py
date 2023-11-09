from django import forms 

class FormularioCarrito(forms.Form):         #formulario para class Cliente del models
    producto = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Producto'}))
    cantidad = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}))
    precio= forms.IntegerField(label="", required=True, widget=forms.NumberInput(attrs={'placeholder': 'Precio'}))

    
class BuscarProductoCarrito(forms.Form):
    producto = forms.CharField(max_length=50, required=False)
    
class EditarProductoCarrito(FormularioCarrito):        
    ...