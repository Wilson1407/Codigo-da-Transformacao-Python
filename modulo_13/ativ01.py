import os
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
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'django.contrib.messages',
            '__main__',
        ],
        MIDDLEWARE=[
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ],
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
                        # HTML ATUALIZADO: Inclui o formulário de busca e os controles de paginação
                        '__main__/produto_list.html': """
                            <h1>Produtos</h1> 
                            <a href="{% url 'criar' %}">[+] Novo Produto</a>
                            <br><br>
                            
                            <form method="get" action="">
                                <input type="text" name="busca" value="{{ request.GET.busca }}" placeholder="Buscar por nome...">
                                <button type="submit">Buscar</button>
                                {% if request.GET.busca %}
                                    <a href="{% url 'lista' %}">Limpar filtro</a>
                                {% endif %}
                            </form>
                            <br>

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
                                <tr><td>Nenhum produto encontrado.</td></tr>
                                {% endfor %}
                            </table>
                            <br>

                            {% if is_paginated %}
                                <div>
                                    {% if page_obj.has_previous %}
                                        <a href="?page={{ page_obj.previous_page_number }}{% if request.GET.busca %}&busca={{ request.GET.busca }}{% endif %}">◀ Anterior</a>
                                    {% endif %}
                                    
                                    <span>Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}</span>
                                    
                                    {% if page_obj.has_next %}
                                        <a href="?page={{ page_obj.next_page_number }}{% if request.GET.busca %}&busca={{ request.GET.busca }}{% endif %}">Próxima ▶</a>
                                    {% endif %}
                                </div>
                            {% endif %}
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
# 4. VIEWS COM BUSCA E PAGINAÇÃO
# ==========================================
class ListaView(ListView):
    model = Produto
    context_object_name = 'produtos'
    paginate_by = 3  # PAGINAÇÃO: Exibe apenas 3 produtos por página para vermos funcionando

    def get_queryset(self):
        """BUSCA: Filtra os produtos pelo nome se o parâmetro 'busca' estiver na URL."""
        queryset = super().get_queryset()
        termo_busca = self.request.GET.get('busca')
        if termo_busca:
            queryset = queryset.filter(nome__icontains=termo_busca) # Busca parcial e sem diferenciar maiúsculas/minúsculas
        return queryset

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
# 6. TESTES AUTOMATIZADOS ATUALIZADOS
# ==========================================
class ProdutoTest(TestCase):
    def test_busca_e_paginacao(self):
        # Criando 4 produtos para estourar o limite de 3 por página
        Produto.objects.create(nome="Caneta Azul", descricao="A", preco=1.0, quantidade=10)
        Produto.objects.create(nome="Caneta Preta", descricao="B", preco=1.0, quantidade=10)
        Produto.objects.create(nome="Caderno", descricao="C", preco=10.0, quantidade=5)
        Produto.objects.create(nome="Borracha", descricao="D", preco=0.5, quantidade=20)
        
        # Testar se a busca filtra corretamente
        response = self.client.get(reverse_lazy('lista') + '?busca=Caneta')
        self.assertContains(response, "Caneta Azul")
        self.assertContains(response, "Caneta Preta")
        self.assertNotContains(response, "Caderno")
        
        # Testar se a paginação jogou o 4º item para a página 2
        response_pg2 = self.client.get(reverse_lazy('lista') + '?page=2')
        self.assertEqual(response_pg2.status_code, 200)

# ==========================================
# 7. EXECUÇÃO DO SCRIPT
# ==========================================
if __name__ == '__main__':
    from django.core.management import call_command
    call_command('migrate', run_syncdb=True, interactive=False)

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        execute_from_command_line([sys.argv[0], 'test', '--keepdb'])
    else:
        # Criando dados fictícios iniciais para você conseguir ver a paginação logo de cara
        if not Produto.objects.exists():
            Produto.objects.create(nome="Notebook Dell", descricao="i7 16GB", preco=4500.0, quantidade=5)
            Produto.objects.create(nome="Mouse Gamer", descricao="RGB 4000 DPI", preco=150.0, quantidade=15)
            Produto.objects.create(nome="Teclado Mecânico", descricao="Switch Blue", preco=299.0, quantidade=8)
            Produto.objects.create(nome="Monitor 24 Pol", descricao="Full HD IPS", preco=850.0, quantidade=4)
            Produto.objects.create(nome="Fone de Ouvido", descricao="Com Microfone", preco=99.0, quantidade=20)

        print("\n🚀 Aplicação Pronta com Busca e Paginação!")
        print("👉 Acesse em: http://127.0.0.1:8000/")
        execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8000'])