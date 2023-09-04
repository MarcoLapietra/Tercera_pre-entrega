from django import forms


class CursoFormulario(forms.Form):
    curso=forms.CharField(required=True)
    profesor=forms.CharField(required=True)



class MayoristaFormulario(forms.Form):
    nombre=forms.CharField(required=True)
    telefono=forms.IntegerField(required=True)
    nroMayorista=forms.CharField(required=True)


