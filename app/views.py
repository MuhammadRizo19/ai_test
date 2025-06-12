from django.shortcuts import render, redirect
from .models import Product

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        is_available = request.POST.get('is_available') == 'on'
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            category=category,
            is_available=is_available,
            image=image
        )
        return redirect('product_create')

    return render(request, 'product_create.html')
