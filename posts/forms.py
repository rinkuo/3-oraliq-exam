from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'image', 'category', 'author', 'description', 'tag']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter the post description here...',
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'rows': 5,
            }),
            'tag': forms.SelectMultiple(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Post title',
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'file-input bg-gray-100 border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline',
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Enter your comment here...', 'rows': 4, 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'comment': 'Your Comment',
        }
        label_attrs = {
            'class': 'block text-gray-700 text-sm font-bold mb-2',
        }
