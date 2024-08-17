from .models import Posts
from django.forms import ModelForm, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'synopsis', 'review']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название фильма'}),
            'synopsis': TextInput(attrs={'class': 'form-control', 'placeholder': 'О чем фильм - ояень кратко'}),
            'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв о фильме'})
        }