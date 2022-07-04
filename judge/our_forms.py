from django import forms
from .models import solution,problem

class code_form(forms.ModelForm):
    code = forms.CharField(widget = forms.Textarea)
    class  Meta:
        model = solution
        fields = ['code']
    # code = forms.CharField(label='Enter your code here',widget= forms.Textarea)
    # curr_problem = forms.ModelChoiceField(problem.objects.all())

# class code_form(forms.Form):
#     curr_problem = forms.ModelChoiceField(problem.objects.all())
#     code=forms.CharField(widget=forms.Textarea)
