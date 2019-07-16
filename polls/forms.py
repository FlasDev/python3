from django import forms


class CalcForm(forms.Form):
    num1 = forms.DecimalField(label='Первое число', min_value=0, max_value=360)
    sign = forms.ChoiceField(label='Знак', choices=[('+',  '+'), ('-', '-'), ('*', '*'), ('/', '/'), ('cos', 'cos')])
    num2 = forms.DecimalField(label='Второе число', min_value=0, max_value=360)
    accurancy = forms.DecimalField(label='Точность', min_value=1, max_value=10)
