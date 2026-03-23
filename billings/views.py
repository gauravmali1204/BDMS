from django.shortcuts import render,redirect,get_object_or_404
from .models import Invoice,payment
from orders.models import order
from django.utils.crypto import get_random_string

# Create your views here.

def invoice_list(request):
    invoices = Invoice.objects.all().order_by('-created_at')
    return render(request, 'billings/invoice_list.html', {'invoices': invoices})

def generate_invoice(request,order_id):
    order_obj = get_object_or_404(order,id=order_id)

    # Check if invoice already exists
    if Invoice.objects.filter(order=order_obj).exists():
        existing_invoice = Invoice.objects.get(order=order_obj)
        return redirect('invoice_detail', existing_invoice.pk)

    gst_amount = (order_obj.total_amount*18)/100
    total = order_obj.total_amount + gst_amount

    invoice = Invoice.objects.create(
        order=order_obj,
        invoice_number=f"INV-{get_random_string(6)}",
        gst_amount=gst_amount,
        total_amount=total
    )
    order_obj.status='COMPLETED'
    order_obj.save()

    return redirect('invoice_detail',invoice.id)


def invoice_detail(request,pk):
    invoice = get_object_or_404(Invoice,pk=pk)
    payments = invoice.payments.all()
    paid_amount =sum(p.amount for p in payments)
    due_amount = invoice.total_amount-paid_amount

    return render(request,'billings/invoice_detail.html',{
        'invoice':invoice,
        'payments':payments,
        'paid_amount':paid_amount,
        'due_amount':due_amount
    })


def add_payment(request,invoice_id):
    invoice = get_object_or_404(Invoice,id=invoice_id)

    if request.method == 'POST':
        payment.objects.create(
            invoice=invoice,
            amount=request.POST.get('amount'),
            payment_mode = request.POST.get('payment_mode')
        )
        return redirect('invoice_detail',invoice.id)
    return render(request,'billings/add_payment.html',{'invoice':invoice})