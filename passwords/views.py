from .models import PasswordEntry, PasswordURL
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PasswordEntryForm, PasswordURLForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'passwords/login.html', {'error_message': error_message})


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
def password_url_create(request):

    if request.method == 'POST':
        form = PasswordURLForm(request.POST)
        if form.is_valid():
            url = form.save()
            messages.success(request, 'Password URL Added Successfully!')
            return redirect('password-url-list')
        else:
            messages.error(request, 'Invalid Form Data. Please Try Again.')
    else:
        form = PasswordURLForm()

    context = {'form': form}
    return redirect(request, 'passwords/password_url_form.html', context)




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