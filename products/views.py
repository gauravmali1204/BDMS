from django.shortcuts import render,redirect,get_object_or_404
from .models import products
from .forms import productform

# Create your views here.
def product_list(request):
    product = products.objects.filter(is_active=True)
    return render (request,'product/product_list.html',{'products':product})

def product_create(request):
    form = productform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'product/product_form.html',{'form':form})

def product_update(request,pk):
    product_obj = get_object_or_404(products,pk=pk)
    form = productform(request.POST or None,instance=product_obj)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'product/product_form.html',{'form':form})

def product_delete(request,pk):
    product_obj = get_object_or_404(products,pk=pk)
    product_obj.is_active=False
    product_obj.save()
    return redirect('product_list')