from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, UpdateView, TemplateView, CreateView, DeleteView)

from teams.forms import TeamForm

from .models import Team
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ListMemberView(ListView):
    model = Team
    template_name = 'teams/members_list.html'
    context_object_name = 'teams'

class AddMemberView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/create_member.html'
    success_url = reverse_lazy('teams:list_teams')


class UpdateMemberView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/update_member.html'
    success_url = reverse_lazy('teams:list_teams')


class DeleteMemberView(DeleteView):
    model = Team
    template_name = 'teams/delete_member.html'
    success_url = reverse_lazy('teams:list_teams')