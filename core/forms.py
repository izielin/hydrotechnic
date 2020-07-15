from django import forms
from .models import Paragraph


class ParagraphForm(forms.ModelForm):
    subtitle = forms.CharField(required=False)

    class Meta:
        model = Paragraph
        fields = ['title', 'subtitle', 'content', ]
