import re

from django import forms
from django.forms import ModelForm

from .models import *

class RuleConditionForm(ModelForm):

    class Meta:
        model = RuleCondition
        fields = ('condition', 'key', 'operation', 'value',)
        widgets = {
            'value': forms.Textarea(attrs={'rows': 1}),
            'description': forms.TextInput()
        }

    def clean(self):
        form_data       = self.cleaned_data
        if form_data['operation'] in ['range', '!range']:
            form_data['value'] = form_data['value'].replace('\n', ' ').replace('\r', '')
            matchObj = re.search(r'[^0-9,~ ]+', form_data['value'])
            if matchObj:
                raise forms.ValidationError(u'Allowed Characters : Digits and ~ when selecting Range or !Range')
        return form_data

class RuleActionForm(ModelForm):

    class Meta:
        model = RuleAction
        fields = ('action', 'key', 'value', )
        widgets = {
            'value': forms.Textarea(attrs={'rows': 1}),
            'description': forms.TextInput()
        }