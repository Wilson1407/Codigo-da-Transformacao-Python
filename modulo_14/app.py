
#import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django.urls import path, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import admin
from django.test import TestCase

# ==========================================
# 1. CONFIGURAÇÕES DO DJANGO (SETTINGS)
# ==========================================
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='chave-secreta-e-simples',
        ROOT_URLCONF=__name__,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',  # Banco de dados em memória RAM
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'django.contrib.messages',
            '__main__',  # Aponta para este próprio arquivo
        ],
        MIDDLEWARE=[
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ],
        # CORREÇÃO: Injetamos os templates diretamente na configuração base do Django
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': False,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'loaders': [
                    ('django.template.loaders.locmem.Loader', {
                        '__main__/produto_list.html': """
                            <h1>Produtos</h1> <a href="{% url 'criar' %}">[+] Novo Produto</a>
                            <hr>
                            <table border="1" cellpadding="5" cellspacing="0">
                                {% for p in produtos %}
                                <tr>
                                    <td><b>{{ p.nome }}</b> - R${{ p.preco }} (Estoque: {{ p.quantidade }})</td>
                                    <td>
                                        <a href="{% url 'editar' p.pk %}">Editar</a> | 
                                        <a href="{% url 'deletar' p.pk %}">Excluir</a>
                                    </td>
                                </tr>
                                {% empty %}
                                <tr><td>Nenhum produto cadastrado.</td></tr>
                                {% endfor %}
                            </table>
                        """,
                        '__main__/produto_form.html': """
                            <h1>{% if object %}Editar{% else %}Criar{% endif %} Produto</h1>
                            <form method="post">{% csrf_token %}{{ form.as_p }}<button type="submit">Salvar</button></form>
                            <br><a href="{% url 'lista' %}">Voltar</a>
                        """,
                        '__main__/produto_confirm_delete.html': """
                            <h1>Excluir Produto</h1>
                            <p>Tem certeza que deseja excluir o produto <strong>{{ object.nome }}</strong>?</p>
                            <form method="post">{% csrf_token %}<button type="submit">Sim, excluir</button></form>
                            <br><a href="{% url 'lista' %}">Cancelar</a>
                        """,
                    }),
                ],
            },
        }],
    )

# Inicializa o Django após as configurações estarem prontas
import django
django.setup()

# ==========================================
# 2. MODELO (BANCO DE DADOS)
# ==========================================
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()

    class Meta:
        app_label = '__main__'

    def __str__(self):
        return self.nome

# ==========================================
# 3. PAINEL DE ADMINISTRAÇÃO
# ==========================================
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')

# ==========================================
# 4. VIEWS (LÓGICA DO CRUD)
# ==========================================
class ListaView(ListView):
    model = Produto
    context_object_name = 'produtos'

class CriarView(CreateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('lista')

class EditarView(UpdateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('lista')

class DeletarView(DeleteView):
    model = Produto
    success_url = reverse_lazy('lista')

# ==========================================
# 5. ROTAS (URLS)
# ==========================================
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaView.as_view(), name='lista'),
    path('novo/', CriarView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditarView.as_view(), name='editar'),
    path('deletar/<int:pk>/', DeletarView.as_view(), name='deletar'),
]

# ==========================================
# 6. TESTES AUTOMATIZADOS
# ==========================================
class ProdutoTest(TestCase):
    def test_fluxo_crud(self):
        # Testar Criação via ORM
        p = Produto.objects.create(nome="Caneta", descricao="Azul", preco=2.50, quantidade=100)
        self.assertEqual(Produto.objects.count(), 1)
        
        # Testar Requisição HTTP na rota de Listagem
        response = self.client.get(reverse_lazy('lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Caneta")

# ==========================================
# 7. EXECUÇÃO DO SCRIPT
# ==========================================
if __name__ == '__main__':
    from django.core.management import call_command
    
    # Cria as tabelas necessárias no banco em memória para o app rodar instantaneamente
    call_command('migrate', run_syncdb=True, interactive=False)

    # Se passar 'test', roda a suíte de testes. Caso contrário, inicia o servidor.
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        execute_from_command_line([sys.argv[0], 'test', '--keepdb'])
    else:
        print("\n🚀 Aplicação Pronta! Acesse o CRUD em: http://127.0.0.1:8000/")

#import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django.urls import path, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import admin
from django.test import TestCase

# ==========================================
# 1. CONFIGURAÇÕES DO DJANGO (SETTINGS)
# ==========================================
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='chave-secreta-e-simples',
        ROOT_URLCONF=__name__,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',  # Banco de dados em memória RAM
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'django.contrib.messages',
            '__main__',  # Aponta para este próprio arquivo
        ],
        MIDDLEWARE=[
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ],
        # CORREÇÃO: Injetamos os templates diretamente na configuração base do Django
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': False,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'loaders': [
                    ('django.template.loaders.locmem.Loader', {
                        '__main__/produto_list.html': """
                            <h1>Produtos</h1> <a href="{% url 'criar' %}">[+] Novo Produto</a>
                            <hr>
                            <table border="1" cellpadding="5" cellspacing="0">
                                {% for p in produtos %}
                                <tr>
                                    <td><b>{{ p.nome }}</b> - R${{ p.preco }} (Estoque: {{ p.quantidade }})</td>
                                    <td>
                                        <a href="{% url 'editar' p.pk %}">Editar</a> | 
                                        <a href="{% url 'deletar' p.pk %}">Excluir</a>
                                    </td>
                                </tr>
                                {% empty %}
                                <tr><td>Nenhum produto cadastrado.</td></tr>
                                {% endfor %}
                            </table>
                        """,
                        '__main__/produto_form.html': """
                            <h1>{% if object %}Editar{% else %}Criar{% endif %} Produto</h1>
                            <form method="post">{% csrf_token %}{{ form.as_p }}<button type="submit">Salvar</button></form>
                            <br><a href="{% url 'lista' %}">Voltar</a>
                        """,
                        '__main__/produto_confirm_delete.html': """
                            <h1>Excluir Produto</h1>
                            <p>Tem certeza que deseja excluir o produto <strong>{{ object.nome }}</strong>?</p>
                            <form method="post">{% csrf_token %}<button type="submit">Sim, excluir</button></form>
                            <br><a href="{% url 'lista' %}">Cancelar</a>
                        """,
                    }),
                ],
            },
        }],
    )

# Inicializa o Django após as configurações estarem prontas
import django
django.setup()

# ==========================================
# 2. MODELO (BANCO DE DADOS)
# ==========================================
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()

    class Meta:
        app_label = '__main__'

    def __str__(self):
        return self.nome

# ==========================================
# 3. PAINEL DE ADMINISTRAÇÃO
# ==========================================
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')

# ==========================================
# 4. VIEWS (LÓGICA DO CRUD)
# ==========================================
class ListaView(ListView):
    model = Produto
    context_object_name = 'produtos'

class CriarView(CreateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('lista')

class EditarView(UpdateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('lista')

class DeletarView(DeleteView):
    model = Produto
    success_url = reverse_lazy('lista')

# ==========================================
# 5. ROTAS (URLS)
# ==========================================
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaView.as_view(), name='lista'),
    path('novo/', CriarView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditarView.as_view(), name='editar'),
    path('deletar/<int:pk>/', DeletarView.as_view(), name='deletar'),
]

# ==========================================
# 6. TESTES AUTOMATIZADOS
# ==========================================
class ProdutoTest(TestCase):
    def test_fluxo_crud(self):
        # Testar Criação via ORM
        p = Produto.objects.create(nome="Caneta", descricao="Azul", preco=2.50, quantidade=100)
        self.assertEqual(Produto.objects.count(), 1)
        
        # Testar Requisição HTTP na rota de Listagem
        response = self.client.get(reverse_lazy('lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Caneta")

# ==========================================
# 7. EXECUÇÃO DO SCRIPT
# ==========================================
if __name__ == '__main__':
    from django.core.management import call_command
    
    # Cria as tabelas necessárias no banco em memória para o app rodar instantaneamente
    call_command('migrate', run_syncdb=True, interactive=False)

    # Se passar 'test', roda a suíte de testes. Caso contrário, inicia o servidor.
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        execute_from_command_line([sys.argv[0], 'test', '--keepdb'])
    else:
        print("\n🚀 Aplicação Pronta! Acesse o CRUD em: http://127.0.0.1:8000/")
        
        execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8000'])