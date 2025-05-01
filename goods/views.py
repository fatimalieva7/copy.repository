# from django.shortcuts import render
from goods.models import Products
from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator


def catalog(request, category_slug):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', 'default')


    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by == order_by != 'default':
        goods = goods.order_by(order_by)
    

    paginator = Paginator(goods, 3)  # 6 товаров на странице
    current_page = paginator.page(int(page))  # Получаем текущую страницу

    context = {
        'title': 'Главная каталог ',
        'goods': current_page,
        'slug_url': category_slug,
        }
    return render(request, 'goods/catalog.html', context)



def product(request,product_slug): #Если передан slug, то product_id не нужен

    context = {
        'product': product,
    }

    return render(request, 'goods/product.html', context)