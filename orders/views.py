from django.shortcuts import render, redirect, get_object_or_404
from .models import order, orderItem
from products.models import products
from custmers.models import custmer

# Create your views here.
def create_order(request):
    custmers = custmer.objects.filter(is_active=True)
    product_list = products.objects.filter(is_active=True)

    if request.method == 'POST':
        custmer_id = request.POST.get('custmer')
        if not custmer_id:
            # Handle error: no customer selected
            pass  # Re-render
        else:
            selected_custmer = get_object_or_404(custmer, id=custmer_id)
            # Proceed with order creation
            orders = order.objects.create(
                custmer=selected_custmer,
                created_by=request.user if request.user.is_authenticated else None
            )

            total = 0
            for p in product_list:
                qty = request.POST.get(f'qty_{p.id}')
                if qty and int(qty) > 0:
                    orderItem.objects.create(
                        order=orders,
                        product=p,
                        quantity=int(qty),
                        price=p.price,
                    )
                    total += int(qty) * p.price

            if total > 0:
                orders.total_amount = total
                orders.save()
                # Instead of redirect, render the list directly
                all_orders = order.objects.all().order_by('-created_at')
                return render(request, 'orders/order_list.html', {'orders': all_orders})
            else:
                orders.delete()
                # No items selected

    return render(request, 'orders/create_order.html', {
        'custmers': custmers,
        'products': product_list,
    })

def order_list(request):
    orders = order.objects.all().order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})