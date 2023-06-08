from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from captcha.fields import CaptchaField
from django.forms import ModelForm
from core.models import Cliente, Fabricante, Veiculo, TabelaPreco, Rotativo, Mensalista


class FormCliente(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Cliente
        fields = "__all__"


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = "__all__"


class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = "__all__"

class FormTabelaPreco(ModelForm):
    class Meta:
        model = TabelaPreco
        fields = "__all__"

class FormRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = "__all__"
        widgets = {
            'data_hora_entrada': DateTimePickerInput(options={"format": "DD/MM/YYYY hh:mm"}),
            'data_hora_saida': DateTimePickerInput(options={"format": "DD/MM/YYYY hh:mm"}),
        }


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = "__all__"