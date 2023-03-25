from django import forms
from .models import Cust, bran


class MyForm(forms.ModelForm):
    genders = (('Male','Male'),('Female','Female'))
    gender = forms.ChoiceField(choices=genders, widget=forms.RadioSelect)

    acctype_choices = (
        ('save', 'Savings Account'),
        ('current', 'Current Account'),
    )
    Account_type = forms.ChoiceField(choices=acctype_choices, widget=forms.Select)
    Cheque_book = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    Debit_Card = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    Credit_Card = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    class Meta:
        model = Cust
        fields = '__all__'
        widgets = { 
            'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'Email': forms.TextInput(attrs={ 'class': 'form-control' }),
            'age': forms.NumberInput(attrs={ 'class': 'form-control ' }),
            'Date_of_Birth': forms.DateInput(attrs={ 'class': 'form-control ' ,'type':'date'}),
            'gender': forms.RadioSelect(attrs={ 'class': 'form-check-input' }),
            'Phone_Number': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
            'District': forms.Select(attrs={ 'class': 'form-select' }),
            'Branch': forms.Select(attrs={ 'class': 'form-select' }),
            'Account_type': forms.Select(attrs={ 'class': 'form-control ' }),
        }    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Branch'].queryset = bran.objects.none()

        if 'District' in self.data:
            try:
                district_id = int(self.data.get('District'))
                self.fields['Branch'].queryset = bran.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['Branch'].queryset = self.instance.district.Branch_set.order_by('name')
