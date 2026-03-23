from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from custmers.models import custmer
from products.models import products
from orders.models import order
from billings.models import Invoice, payment
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models import Q


@login_required
def dashboard(request):
    total_customers = custmer.objects.filter(is_active=True).count()
    total_products = products.objects.filter(is_active=True).count()
    total_orders = order.objects.count()

    total_revenue = Invoice.objects.aggregate(
        Sum('total_amount')
    )['total_amount__sum'] or 0

    total_paid = payment.objects.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    pending_amount = total_revenue - total_paid

    recent_orders = order.objects.order_by('-created_at')[:5]

    return render(request, 'reports/dashboard.html', {
        'total_customers': total_customers,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_amount': pending_amount,
        'recent_orders': recent_orders,
    })


@login_required
def search_view(request):
    query = request.GET.get('q', '')
    results = {
        'customers': [],
        'products': [],
        'orders': [],
        'invoices': [],
    }
    
    if query:
        # Search customers
        results['customers'] = custmer.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(phone__icontains=query)
        ).filter(is_active=True)[:10]
        
        # Search products
        results['products'] = products.objects.filter(
            Q(name__icontains=query) | 
            Q(product_type__icontains=query) |
            Q(stock_unit__icontains=query)
        ).filter(is_active=True)[:10]
        
        # Search orders
        results['orders'] = order.objects.filter(
            Q(id__icontains=query) |
            Q(custmer__name__icontains=query)
        )[:10]
        
        # Search invoices
        results['invoices'] = Invoice.objects.filter(
            Q(invoice_number__icontains=query) |
            Q(order__custmer__name__icontains=query)
        )[:10]
    
    return render(request, 'reports/search.html', {
        'query': query,
        'results': results,
    })



monthly_revenue = (
    Invoice.objects
    .annotate(month=TruncMonth('created_at'))
    .values('month')
    .annotate(total=Sum('total_amount'))
    .order_by('month')
)




