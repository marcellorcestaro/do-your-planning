""" Gastos Fixos, Variáveis, Adicionais e Reserva """

from django.db import models

# Create your models here.
class Fixo(models.Model):
    """Tabela de gastos fixos"""

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    categoria = models.CharField(max_length=140)
    val_esperado = models.FloatField(verbose_name="Valor Esperado")
    val_pago = models.FloatField(verbose_name="Valor Pago")

    def falta_pagar(self):
        """ Retorna o quanto falta para pagar, em relação ao valor esperado e pago"""
        return self.val_esperado - self.val_pago

    def __str__(self):
        return self.nome 
