from django.urls import path
from account.views import AccountHomeView, AccountCreateView, AccountUpdateView, AccountDeleteView, AccountDetailView

app_name = "account"

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('main/create/', AccountCreateView.as_view(), 'create'),
    path('main/<int:pk>/update', AccountUpdateView.as_view(), name='update'),
    path('main/<int:pk>/delete', AccountDeleteView.as_view(), name='delete'),
    path('main/<int:pk>/detail', AccountDetailView.as_view(), name='detail'),
]

