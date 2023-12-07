from django import forms
from .models import CustomUser

class CustomForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields = '__all__'
        widgets={
            'roll_no':forms.TextInput(attrs={"class":'form-control','id':"floatingroll_no", 'placeholder':"roll_no"}),
            'first_name':forms.TextInput(attrs={"class":'form-control','id':"floatingfirst_name", 'placeholder':"first_name"}),
            'last_name':forms.TextInput(attrs={"class":'form-control','id':"floatinglast_name", 'placeholder':"last_name"}),
            'email':forms.TextInput(attrs={"class":'form-control','id':"floatingemail", 'placeholder':"email"}),
            'mobile':forms.TextInput(attrs={"class":'form-control','id':"floatingmobile", 'placeholder':"mobile"}),
            'image':forms.FileInput(attrs={"class":'form-control','id':"image","accept":"*/images","onchange":"selectImage()"}),
        }
        