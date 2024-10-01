from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel  # Replace MyModel with your actual model name
        fields = ['field1', 'field2', 'field3']  # Specify the fields you want in your form

    # Optionally, you can define custom form validation methods here
    def clean_field1(self):
        data = self.cleaned_data['field1']
        # Custom validation logic for field1
        return data

    # Add more custom form validation methods as needed
