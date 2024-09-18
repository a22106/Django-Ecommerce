from django.shortcuts import render
from django.core.paginator import Paginator
from shop.models import Products


# Create your views here.
def index(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get("item_name")
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)
        
    items_per_page = 4
    pagenator = Paginator(product_objects, items_per_page)
    page_number = request.GET.get("page")
    product_objects = pagenator.get_page(page_number)

    return render(request, "shop/index.html", {"product_objects": product_objects})

def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, "shop/detail.html", {"product_object": product_object})
