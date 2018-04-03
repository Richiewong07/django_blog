from django.forms import ModelForm

from .models import Post

class PostForm(ModelForm):
    class Meta:             # INNER CLASS
        model = Post
        fields = [
            "title",
            "content",
            "image"
        ]
