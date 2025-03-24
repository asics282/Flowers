from django.shortcuts import render


def main_page(request):
    return render(request, 'flowers/main.html')


def flower_page(request, flower_name):
    return render(request, f'flowers/{flower_name}')
