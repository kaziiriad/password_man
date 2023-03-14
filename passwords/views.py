tfrom .models import PasswordEntry, PasswordURL
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PasswordEntryForm
from django.contrib.auth.decorators import login_required


@login_required
def password_url_list(request):
    password_urls = PasswordURL.objects.all()
    return render(
        request, 
        'passwords/password_url_list.html', 
        {'password_urls': password_urls}
    )

@login_required
def password_url_detail(request, pk):
    password_url = get_object_or_404(PasswordURL, pk=pk)
    password_entries = password_url.passwordentry_set.all()
    return render(
        request,
        'passwords/password_url_detail.html',
        {'password_url': password_url, 
        'password_entries': password_entries}
    )

@login_required
def password_entry_create(request, pk):
    password_url = get_object_or_404(PasswordURL, pk=pk)
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            password_entry.url = password_url
            password_entry.save()
            return redirect('password_url_detail', pk=password_url.pk)
        else:
            form = PasswordEntryForm()
        return render(request, 'passwords/password_entry_form.html', {'form': form})

@login_required
def password_entry_update(request, pk):
    password_entry = get_object_or_404(PasswordEntry, pk=pk)
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST, instance=password_entry)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            password_entry.save()
            return redirect('password_url_detail', pk=password_entry.url.pk)
    else:
        form = PasswordEntryForm(instance=password_entry)
    return render(request, 'passwords/password_entry_form.html', {'form': form})

@login_required
def password_entry_delete(request, pk):
    password_entry = get_object_or_404(PasswordEntry, pk=pk)
    password_url_pk = password_entry.url.pk
    password_entry.delete()
    return redirect('password_url_detail', pk=password_url_pk)    