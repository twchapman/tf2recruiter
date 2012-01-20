class PlayerForm(forms.ModelForm):
  Meta:
    model = Profile
    exclude ['user']