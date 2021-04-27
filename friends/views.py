from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Friends
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class FriendsListView(ListView):
    model = Friends

class FriendsCreateView(CreateView):
    model = Friends
    fields = ['name','phone','addr','birthday']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class FriendsDetailView(DetailView):
    model = Friends

class FriendsUpdateView(UpdateView):
    model = Friends
    fields = ['name','phone','addr','birthday']
    success_url = reverse_lazy('list')     #대신에 get_absolute_url을 정의하여 사용하기도 함
    template_name_suffix = '_update'

class FriendsDeleteView(DeleteView):
    model = Friends
    fields = ['name','phone','addr','birthday']
    success_url = reverse_lazy('list')
    template_name_suffix = '_confirm_delete'