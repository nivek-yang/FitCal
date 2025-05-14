from django.shortcuts import get_object_or_404, redirect, render

from .forms import StoreForm
from .models import Store


def index(req):
    stores = Store.objects.all()

    if req.method == 'POST':
        form = StoreForm(req.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:show', store.id)
        else:
            return render(req, 'stores/new.html', {'form': form})
    else:
        return render(req, 'stores/index.html', {'stores': stores})


def new(req):
    form = StoreForm()
    return render(req, 'stores/new.html', {'form': form})


def show(req, id):
    store = get_object_or_404(Store, pk=id)

    if req.method == 'POST':
        form = StoreForm(req.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('stores:show', store.id)
        return render(req, 'stores/edit.html', {'store': store, 'form': form})

    else:
        form = StoreForm(instance=store)

        return render(
            req,
            'stores/show.html',
            {'store': store, 'form': form},
        )


def edit(req, id):
    store = get_object_or_404(Store, id=id)
    form = StoreForm(instance=store)
    return render(req, 'stores/edit.html', {'store': store, 'form': form})


def delete(req, id):
    store = get_object_or_404(Store, pk=id)
    store.delete()

    return redirect('stores:index')
