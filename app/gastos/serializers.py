""" Serializadores para a REST API, convertendo dados para JSON """

from rest_framework import serializers
from .models import Fixo

class FixoSerializer(serializers.ModelSerializer):

    """ Serializador para gastos fixos """

    class Meta:

        """ Settings para o serializador de gastos fixos"""

        model = Fixo
        fields = ('id', 'nome', 'dia', 'mes', 'ano', 'categoria',
                  'val_esperado', 'val_pago', 'created_by')
        read_only_fields = ('id', 'created_by',)
