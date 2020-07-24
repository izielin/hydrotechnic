from django import forms
from .models import Paragraph, LINK_CHOICES, Image, Offer, Address, Box


class ParagraphForm(forms.ModelForm):
    subtitle = forms.CharField(required=False)
    link = forms.CharField(required=False)

    class Meta:
        model = Paragraph
        fields = ['title', 'subtitle', 'content', 'link', 'image']

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


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class BoxForm(forms.ModelForm):
    experience = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = Box
        fields = "__all__"
