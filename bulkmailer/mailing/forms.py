from django import forms

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')
    subject = forms.CharField(max_length=100, label='Email Subject')
    message = forms.CharField(widget=forms.Textarea, label='Email Message')