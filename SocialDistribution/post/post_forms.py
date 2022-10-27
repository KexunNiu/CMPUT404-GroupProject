from django import forms
from .models import Post, Comment


class post_form(forms.ModelForm):
    title = forms.CharField(label='title', 
        required = False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Please enter your title',
        })
    )

    description = forms.CharField(label='description',
        required = False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Please enter your description',
        })
    )
    content = forms.CharField(label='content', 
        required = False,
        widget=forms.Textarea(attrs={
            'placeholder': 'If you want to type something',

        })
    )

    Categories = forms.CharField(label='categories',
        required = False,
        widget=forms.Textarea(attrs={
            'placeholder':"You can place your categories here." ,
            'rows':2,

        })
    )
    class Meta:
        model = Post
        fields = ['title', 'description', 'textType', 'content','Categories','visibility']
        

class Comment_form(forms.ModelForm):
    Comment = forms.CharField(label='content', 
        required = False,
        widget=forms.Textarea(attrs={
            'placeholder': 'If you want to comment something',

        })
    )
    class Meta:
        model = Comment
        fields = ['contentType','comment']


# class Like_form(forms.ModelForm):
#     class Meta:
#         model = Like
#         fields = ['like']