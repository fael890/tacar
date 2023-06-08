from django.contrib import admin
from core.models import Cliente,Fabricante,Veiculo, TabelaPreco, Rotativo, Mensalista

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Fabricante)
admin.site.register(Rotativo)
admin.site.register(Mensalista)
admin.site.register(TabelaPreco)
