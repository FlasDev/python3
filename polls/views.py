from django.http import HttpResponseRedirect
from django.shortcuts import render
from polls.forms import CalcForm
import math


def get_data(request):
    result = ''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_obj = CalcForm(request.POST)
        # check whether it's valid:
        if form_obj.is_valid():
            num1 = form_obj.cleaned_data['num1']
            sign = form_obj.cleaned_data['sign']
            num2 = form_obj.cleaned_data['num2']
            accurancy = form_obj.cleaned_data['accurancy']

            if sign == '+':
                result = add(num1, num2, accurancy)
            elif sign == '-':
                result = dif(num1, num2, accurancy)
            elif sign == '*':
                result = multiplier(num1, num2, accurancy)
            elif sign == '/':
                result = devision(num1, num2, accurancy)
            elif sign == 'cos':
                result = degree_to_number(num1)

    # if a GET (or any other method) we'll create a blank form
    else:
        form_obj = CalcForm()

    return render(request, 'templates/calculator.html', {'f': form_obj, 'res': result})


def add(num1, num2, rn):
    return round(num1 + num2, int(rn))

def dif(num1, num2, rn):
    return round(num1 - num2, int(rn))

def multiplier(num1, num2, rn):
    return round(num1 * num2, int(rn))

def devision(num1, num2, rn):
    return round(num1 / num2, int(rn))
def degree_to_number(num1):
    x = math.cos(math.radians(num1))
    return x