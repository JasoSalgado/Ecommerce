# accounts/forms.py
# Django modules
from django import forms

# My modules
from .models import Account

class RegistrationForm(forms.ModelForm):
    """
    Registration form
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Ingrese la contraseña",
        "class": "form-control",
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirme la contraseña",
        "class": "form-control",
    }))

    class Meta:
        model = Account
        fields = ['first_name', 
                'last_name', 
                'phone_number',
                'email', 
                'password']
    

    def __init__(self, *args, **kwargs):
        """
        Not to repeat styles.
        """

        super(RegistrationForm, self).__init__(*args, **kwargs)
        # form labels
        self.fields["first_name"].widget.attrs["placeholder"] = "Ingrese nombre"
        self.fields["last_name"].widget.attrs["placeholder"] = "Ingrese apellido"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Ingrese número de teléfono"
        self.fields["email"].widget.attrs["placeholder"] = "Ingrese correo electrónico"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
    

    def clean(self):
        """
        Validate password if password does not match with confirm_password raises an error
        """
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "La contraseña no coincide."
                )