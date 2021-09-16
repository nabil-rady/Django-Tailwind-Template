from django.shortcuts import render
from django.template import RequestContext


def handler404(request, exception, template_name="pages/404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response

def landing_page(request):
    return render(request, 'pages/base.html')
def dashboard(request):
    return render(request, 'pages/index.html')
def forms(request):
    return render(request, 'pages/forms.html')
def cards(request):
    return render(request, 'pages/cards.html')
def charts(request):
    return render(request, 'pages/charts.html')
def buttons(request):
    return render(request, 'pages/buttons.html')
def modals(request):
    return render(request, 'pages/modals.html')
def tables(request):
    return render(request, 'pages/tables.html')
def login(request):
    return render(request, 'pages/login.html')
def forgot_password(request):
    return render(request, 'pages/forgot-password.html')
def create_account(request):
    return render(request, 'pages/create-account.html')
def blank(request):
    return render(request, 'pages/blank.html')
def template404(request):
    return render(request, 'pages/404.html')