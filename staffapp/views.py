from decimal import Decimal

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from staffapp.forms import ExpenseForm
from staffapp.models import Expenses


# Create your views here.
TOTAL_BUDGET = Decimal('5000.00')

class StaffDashboard(ListView):
    model = Expenses
    template_name = 'staff_dashboard.html'
    context_object_name = 'expenses'


class AddExpense(LoginRequiredMixin, CreateView):
    model = Expenses
    fields = ['description', 'amount', 'date']  # user is NOT included in the form
    template_name = 'addexpense.html'
    success_url = reverse_lazy('remaining_budget')  # redirect after success

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class Remaining_budget(ListView):
    model=Expenses
    template_name = 'remaining_budget.html'
    context_object_name = 'expenses'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        spent = Expenses.objects.aggregate(total_spent=Sum('amount'))['total_spent'] or Decimal('0.00')
        context['remaining_budget']=TOTAL_BUDGET-spent
        context['total_budget']=TOTAL_BUDGET
        context['total_spent'] = spent
        return context

class EditView(UpdateView):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'addexpense.html'
    success_url = reverse_lazy('remaining_budget')

class Delete(DeleteView):
    model= Expenses
    template_name = 'delete.html'
    context_object_name = 'expense'
    success_url = reverse_lazy('remaining_budget')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('staff_dashboard')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
        logout(request)
        return render(request, 'logout.html')








