from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required

def items(request):
    querry = request.GET.get('querry', '')
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    if querry:
        items = items.filter(Q(name__icontains=querry) | Q(description__icontains=querry))
    return render(request, 'item/items.html', {
        'items':items,
    })

def detail(request, pk):
    item=get_object_or_404(Item, pk=pk)
    related_items= Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/details.html', {
        'item': item,
        'related_items': related_items,
        'categories': categories,
    })

@login_required
def new(request):
    if request.method=='POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:

        form = NewItemForm()
    return render(request, 'item/form.html', {
        'form':form,
        'title': 'New Item'
        
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method=='POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:

        form = EditItemForm(instance=item)
    return render(request, 'item/form.html', {
        'form':form,
        'title': 'Edit Item'
        
    })