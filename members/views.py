from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from common.decorator import member_required

from .forms import MemberForm
from .models import Member


def new(req):
    form = MemberForm()
    return render(req, 'members/new.html', {'form': form})


@member_required
@transaction.atomic
def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = request.user
            member.save()
            return redirect('members:show', member.id)
    form = MemberForm()
    return render(request, 'members/new.html', {'form': form}, status=400)


@login_required
@member_required
def index(request):
    member = Member.objects.filter(user=request.user).first()
    return render(request, 'members/index.html', {'member': member})


@login_required
@member_required
def show(request, id):
    member = get_object_or_404(Member, pk=id, user=request.user)
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members:show', member.id)
        return render(request, 'members/show.html', {'member': member, 'form': form})
    return render(request, 'members/show.html', {'member': member})


@login_required
@member_required
def edit(request, id):
    member = get_object_or_404(Member, pk=id, user=request.user)
    form = MemberForm(instance=member)
    return render(request, 'members/edit.html', {'form': form, 'member': member})


@member_required
def delete(request, id):
    member = get_object_or_404(Member, pk=id, user=request.user)
    member.delete()
    # user.delete()
    return redirect('users:sign_up')
