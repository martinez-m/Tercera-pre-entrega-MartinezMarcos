from django import forms
from .models import Producto, Cliente, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'total']  # Excluimos 'fecha', ya que se llena automáticamente
        widgets = {
            'productos': forms.CheckboxSelectMultiple()  # Permite seleccionar múltiples productos
        }