from django import forms
from .models import Post


class AwardLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }
class ProjectUpload(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        