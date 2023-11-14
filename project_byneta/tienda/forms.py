from django import forms 
from .models import Producto
from ckeditor.fields import RichTextFormField


class FormularioProducto(forms.ModelForm):
    nombre = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre del Producto'}))
    descripcion = RichTextFormField()
    precio = forms.DecimalField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Precio'}))
    imagen = forms.ImageField(label="", required=True, widget=forms.ClearableFileInput(attrs={'placeholder': 'Seleccionar Imagen'}))
    cantidad = forms.IntegerField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}))
    tipo = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Tipo de Producto'}))
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
        help_texts = {key: '' for key in fields}
class FormularioAccesorios(forms.ModelForm):    
    nombre = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre del Producto'}))
    descripcion = RichTextFormField()
    precio = forms.DecimalField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Precio'}))
    imagen = forms.ImageField(label="", required=True, widget=forms.ClearableFileInput(attrs={'placeholder': 'Seleccionar Imagen'}))
    cantidad = forms.IntegerField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}))
    tipo = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Tipo de Producto'}))
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
        help_texts = {key: '' for key in fields}
    
class FormularioAutobronceantes(forms.ModelForm):
    nombre = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre del Producto'}))
    descripcion = RichTextFormField()
    precio = forms.DecimalField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Precio'}))
    imagen = forms.ImageField(label="", required=True, widget=forms.ClearableFileInput(attrs={'placeholder': 'Seleccionar Imagen'}))
    cantidad = forms.IntegerField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}))
    tipo = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Tipo de Producto'}))
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
        help_texts = {key: '' for key in fields}
        
class FormularioBrumas(forms.ModelForm):
    nombre = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre del Producto'}))
    descripcion = RichTextFormField()
    precio = forms.DecimalField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Precio'}))
    imagen = forms.ImageField(label="", required=True, widget=forms.ClearableFileInput(attrs={'placeholder': 'Seleccionar Imagen'}))
    cantidad = forms.IntegerField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}))
    tipo = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Tipo de Producto'}))
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']
        help_texts = {key: '' for key in fields}
        




