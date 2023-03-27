from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import Http404, HttpRequest, HttpResponse
from django.contrib.auth.models.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.conf import settings

from account.models import Account
from account.forms import AccountForm, AccountFormModel
# Create your views here.

data = [
    { id: 1, content: 'Helo', result: ''},
    { id: 2, content: 'Mike', result: ''},
    { id: 3, content: 'Value', result: '' },
]

class AccountCreateView(View):
    def post(self, request):
        user = User(email=request.POST.get("email"), first_name=request.POST.get("first_name"), last_name=request.POST.get("last_name"), password=request.POST.get("password"), username=request.POST.get("username"))
        account = Account(age=request.POST.get("age"), authenticated=False, image_field=None)
        account.save()
        return redirect(reverse('account:home'))

class AccountListView(View):
    def get(self, request):
        account = Account.objects.all()
        ctx = {'account': account}
        return render(request, 'account/list.html', ctx)

class AccountDeleteView(View):
    def delete(self, request):
        account = Account.objects.get(id=request.query_params.get("id"))
        account.delete()
        return redirect(reverse('main:home'))

class AccountDetailView(View):
    def get(self, request):
        ctx = { }
        account = Account.objects.get(id=request.query_params.get("id"))
        if account is not None:
            ctx['account'] = account
            return render(request, 'account/detail.html', ctx)

class AccountHomeView(View):
    def post(self, request):
        ctx = {'data': data}
        account = Account.objects.get(user=request.user)
        form = AccountForm(request.POST, or None, request.FILES, or None, instance=account)
        request.set_cookie(key=settings.get_cookie_key(), max_age=settings.get_max_age(), expires=settings.get_expires_date(), path='/', domain=settings.get_domain())
        confirm = False
        if form.is_valid():
            form.save()
            confirm = True

        ctx = {
            'account': account,
            'form': form,
            'confirm': confirm
        }

        return render(request, 'account/home.html', ctx)
