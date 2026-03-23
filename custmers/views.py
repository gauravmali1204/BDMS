from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.permissions import staff_required
from .models import custmer
from .forms import CustmerForm


# Create your views here.
@login_required
@staff_required
def custmer_list(request):
    custmers = custmer.objects.filter(is_active=True)
    return render(request,'custmer/custmer_list.html',{'custmers':custmers})

@login_required
@staff_required
def custmer_create(request):
    form=CustmerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('custmer_list')
    return render (request,'custmer/custmer_form.html',{'form':form})

@login_required
@staff_required
def custmer_update(request,pk):
    custmer_obj=get_object_or_404(custmer,pk=pk)
    form=CustmerForm(request.POST or None, instance=custmer_obj)
    if form.is_valid():
        form.save()
        return redirect('custmer_list')
    return render (request,'custmer/custmer_form.html',{'form':form})

@login_required
@staff_required
def custmer_delete(request,pk):
    custmer_obj=get_object_or_404(custmer,pk=pk)
    custmer_obj.is_active=False
    custmer_obj.save()
    return redirect('custmer_list')