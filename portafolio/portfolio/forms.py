from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model= ContactMessage
        fields= ["name", "email", "message"]
        labels= {
            "name": "Nombre",
            "email": "Correo",
            "message": "Comentario",
        }

        widgets= {
            "name": forms.TextInput(attrs= {"placeholder": "Tu nombre"}),
            "email": forms.EmailInput(attrs= {"placeholder": "tucorreo@ejemplo.com"}),
            "message": forms.Textarea(attrs= {"placeholder": "Escribe tu comentario", "rows": 5}),
        }