from django import forms
from accounts.models import CustomUser

class RegistrationForm(forms.ModelForm):
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput())
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields=('email','first_name','last_name','location','password1','password2')
        
        labels={'email':'email','first_name':'firstname','last_name':'lastname','location':'location','password1':'password2'}
        
        help_texts={'email':'enter your correct email','first_name':'enter your first name','last_name':'enter your last name'}
        
        def clean_password2(self):
            p1=self.cleaned_data.get('password1')
            p2=self.cleaned_data.get('password2')
            
            if p1 and p2 and p1!=p2:
                raise forms.ValidationError('password dont match')
            return p2
        
        def clean_email(self):
            email=self.cleaned_data.get('email')
            user=CustomUser.objects.get(email=email)
            if user:
                raise forms.ValidationError('email already exists')
            
class loginform(forms.Form):
    email=forms.EmailField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    
            