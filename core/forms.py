from django import forms
from .models import Paragraph, LINK_CHOICES, Image, Offer


class ParagraphForm(forms.ModelForm):
    subtitle = forms.CharField(required=False)
    link = forms.CharField(required=False)

    class Meta:
        model = Paragraph
        fields = ['title', 'subtitle', 'content', 'link']

    def __init__(self, *args, **kwargs):
        super(ParagraphForm, self).__init__(*args, **kwargs)
        self.fields['link'].choices = LINK_CHOICES


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = "__all__"


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)
