from django import forms


class VentasFormulario(forms.Form):
    
    producto = forms.CharField(required=True)
    precio  = forms.IntegerField()