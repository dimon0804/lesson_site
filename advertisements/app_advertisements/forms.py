from django import forms 
from .models import Advertisements

class AdForm(forms.Form):
    title = forms.CharField(max_length=64, widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
    price = forms.DecimalField(widget = forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})) 
# class AdForm(forms.ModelForm):
#     class Meta:
#         model = Advertisements
#         fields = '__all__'

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
#            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
#             'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
#             'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }

#     def clean_title(self):
#         title = self.cleaned_data.get('title')
#         if title and title.startswith('?'):
#             raise forms.ValidationError('Заголовок не может начинаться с вопросительного знака')
#         return title