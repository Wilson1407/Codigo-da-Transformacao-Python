# Adicione uma busca por nome na listagem de produtos e implemente paginação para melhorar a navegação.
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django.urls import path, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import admin
from django.test import TestCase
