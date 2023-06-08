"""tacar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('captcha/', include('captcha.urls')),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('listagem_clientes/', listagem_clientes, name='url_listagem_clientes'),
    path('atualizar_cliente/<int:id>/', atualizar_cliente, name='url_atualiza_cliente'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculos/', listagem_veiculos, name='url_listagem_veiculos'),
    path('atualizar_veiculo/<int:id>/', atualiza_veiculo, name='url_atualiza_veiculo'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('cadastro_fabricante/', cadastro_fabricante, name='url_cadastro_fabricante'),
    path('listagem_fabricantes/', listagem_fabricantes, name='url_listagem_fabricantes'),
    path('exclui_fabricante/<int:id>/', exclui_fabricante, name='url_exclui_fabricante'),
    path('cadastro_tabela/', cadastro_tabela, name='url_cadastro_tabela'),
    path('listagem_tabelas/', listagem_tabelas, name='url_listagem_tabelas'),
    path('exclui_tabela/<int:id>/', exclui_tabela, name='url_exclui_tabela'),
    path('listagem_rotativos/', listagem_rotativos, name='url_listagem_rotativos'),
    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativo'),
    path('atualiza_rotativo/<int:id>/', atualiza_rotativo, name='url_atualiza_rotativo'),
    path('exlui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),
    path('listagem_mensalistas/', listagem_mensalistas, name='url_listagem_mensalistas'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalista'),
    path('atualiza_mensalista/<int:id>/', atualiza_mensalista, name='url_atualiza_mensalista'),
    path('exlui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
