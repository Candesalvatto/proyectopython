from django import forms 
from .models import Producto


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
class FormularioAccesorios(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [ 'nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
    
class FormularioAutobronceantes(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [ 'nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
        
class FormularioBrumas(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [ 'nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
        




