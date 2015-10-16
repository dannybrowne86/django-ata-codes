from django import forms
from django.forms import widgets

from timepiece.utils.search import SearchForm

from .models import ATACode

class AddEditATACode(forms.ModelForm):

    class Meta:
        model = ATACode
        fields = ('primary_ata_code', 'secondary_ata_code', 'name',
            'severity_factor', 'last_change_date')

    # def __init__(self, *args, **kwargs):
    #     super(AddEditATACode, self).__init__(*args, **kwargs)

class ATACodeSearchForm(SearchForm):
    primary_ata_code = forms.IntegerField(required=False, label='')

    def __init__(self, *args, **kwargs):
        super(ATACodeSearchForm, self).__init__(*args, **kwargs)
        self.fields['primary_ata_code'].widget.attrs['placeholder'] = 'ATA'
        self.fields['primary_ata_code'].widget.attrs['size'] = "4"
