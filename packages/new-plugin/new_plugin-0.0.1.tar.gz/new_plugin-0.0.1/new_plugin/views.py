from testy.core.models import Project

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView
from rest_framework.generics import CreateAPIView

class ProjectListView(ListView):
    model = Project
    template_name = 'new_plugin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context
