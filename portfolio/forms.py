from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "budget", "comment"]
        labels = {
            "name": "To'liq ismingiz",
            "email": "Email manzilingiz",
            "subject": "Mavzu",
            "budget": "Taklif etilayotgan byudjet",
            "comment": "Izohingiz",
        }
        help_texts = {
            "comment": "Iltimos, so'rovingiz haqida batafsil ma'lumot kiriting.",
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        subject = cleaned_data.get("subject")
        budget = cleaned_data.get("budget")
        comment = cleaned_data.get("comment")

        # Name validation
        if name:
            if not name.isalpha():
                self.add_error("name", "Ism faqat harflardan iborat bo'lishi kerak.")
            if len(name) < 2:
                self.add_error("name", "Ism kamida 2 ta belgidan iborat bo'lishi kerak.")

        # Email validation
        if email:
            try:
                validate_email(email)
            except ValidationError:
                self.add_error("email", "Iltimos, haqiqiy email manzil kiriting.")

        # Subject validation
        if subject:
            if len(subject) < 5:
                self.add_error("subject", "Mavzu kamida 5 ta belgidan iborat bo'lishi kerak.")

        # Budget validation
        if budget:
            if not isinstance(budget, (int, float)):
                self.add_error("budget", "Byudjet raqam bo'lishi kerak.")
            elif budget <= 0:
                self.add_error("budget", "Byudjet 0 dan katta bo'lishi kerak.")

        # Comment validation
        if comment:
            if len(comment) < 10:
                self.add_error("comment", "Izoh kamida 10 ta belgidan iborat bo'lishi kerak.")

        return cleaned_data