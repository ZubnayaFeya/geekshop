from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    products = {}
    context = {
        'page_title': 'Каталог товаров'
    }
    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '123-45-67',
            'email': 'name@domain.com',
            'address': 'Интернет'
        }
    ]
    context = {
        'page_title': 'Контакты',
        'locations': locations
    }
    return render(request, 'mainapp/contacts.html', context)


def basket(request):
    context = {
        'page_title': 'Корзина'
    }
    return render(request, 'mainapp/basket.html', context)
