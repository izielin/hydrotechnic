from django import forms
from .models import Paragraph, LINK_CHOICES


class ParagraphForm(forms.ModelForm):
    subtitle = forms.CharField(required=False)
    link = forms.CharField(required=False)

    class Meta:
        model = Paragraph
        fields = ['title', 'subtitle', 'content', 'link']

    def __init__(self, *args, **kwargs):
        super(ParagraphForm, self).__init__(*args, **kwargs)
        self.fields['link'].choices = LINK_CHOICES
