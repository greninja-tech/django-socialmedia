from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','image')
        
        labels={'title':'title','content':'content','image':'image'}
        
        help_texts={'title':'enter title of your post','content':'enter your content of post','image':'Upload your image'}
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }