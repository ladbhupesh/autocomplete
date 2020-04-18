from django import forms

from geocode.models import Coordinate, Profiles

# dont change atrrs
class CoordinateForm(forms.ModelForm):
    code = forms.CharField(max_length=150,
                           label='',
                           widget=forms.TextInput(
                               attrs={
                                   'autocomplete': 'off',
                                   "onkeyup":"getGeoCode(this.value)",
                                    "list":"mylist"
                               },
                           ))
    class Meta:
        model = Coordinate
        fields = "__all__"
    class Media:
        js = ('jquery.js','autocomplete.js')

    def clean_code(self):
            code=self.cleaned_data.get("code")
            if not Profiles.objects.filter(geocode=code).exists():
                raise forms.ValidationError ( "Not true")
            return code