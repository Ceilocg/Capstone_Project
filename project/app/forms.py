from django import forms
from django.contrib.auth.models import User
from .models import ExcelFile




class CertificateRequestForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your full name'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    lrn = forms.CharField(label='LRN Number', max_length=12, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your LRN number'
    }))
    certificate_type = forms.ChoiceField(label='Certificate Type', choices=[
        ('Certification', 'Certification'),
        ('Form 137', 'Form 137'),
        ('Form 138', 'Form 138'),
        ('good_moral', 'Good Moral Certificate'),
    ], widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    request_purpose = forms.CharField(label='Request Purpose', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'State the purpose of the request',
        'rows': 3
    }))

class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class ExcelFileForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file', 'name']