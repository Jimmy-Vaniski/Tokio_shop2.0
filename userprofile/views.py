from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def vendor_details(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/vendor_details.html', {'user': user})


def my_shop(request):
    return render(request, 'userprofile/my_shop.html')


def my_account(request):
    return render(request, 'userprofile/my_account.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            userprofile = UserProfile.objects.create(user=user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()
    return render(request, 'userprofile/register.html', {'form': form})
