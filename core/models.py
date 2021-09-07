from django.db import models

# Create your models here.


class Base(models.Model):
    criado = models.DateField('criacao', auto_now_add=True)
    atualizado = models.DateField('atualizado', auto_now=True)

    class Meta:
        abstract = True


class Meeiro(Base):
    __tablename__ = 'meeiro'

    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, max_length=250)
    cpf = models.CharField(null=False, unique=True, max_length=15)
    rg = models.CharField(null=False, max_length=15)

    models.UniqueConstraint(fields=['id', 'cpf'], name='meeiro_unique_constraint')

    class Meta:
        verbose_name = 'Meeiro'
        verbose_name_plural = 'Meeiros'

    def __repr__(self):
        return "<Meeiro(name='%s', cpf='%s', rg='%s')>" % (self.name, self.cpf, self.rg)


class Client(Base):
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clientes de Venda'

    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, max_length=250)

    def __repr__(self):
        return "<Client(name='%s')>" % self.name


class EntryType(Base):
    class Meta:
        verbose_name = 'Tipo de lançamento'
        verbose_name_plural = 'Tipos de lançamentos'

    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(null=False, max_length=500)


class Entry(Base):
    """
        Lançamentos de meeiros
    """

    class Meta:
        verbose_name = 'Lançamento'
        verbose_name_plural = 'Lançamentos de Meeiros'

    id = models.IntegerField(primary_key=True, auto_created=True)
    meeiro_id = models.ForeignKey(Meeiro, null=False, on_delete=models.DO_NOTHING)
    entry_date = models.DateField(null=False)
    entry_type = models.ForeignKey(EntryType, null=False, on_delete=models.DO_NOTHING)
    entry_value = models.FloatField(null=False)
    description = models.CharField(null=False, max_length=500)


class SalesEntry(Base):
    """
    Lançamentos de compra e venda
    """

    class Meta:
        verbose_name = 'Lançamento de venda'
        verbose_name_plural = 'Lançamentos de venda'

    id = models.IntegerField(primary_key=True, auto_created=True)
    client_id = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    entry_date = models.DateField(null=False)
    sales_price = models.FloatField(null=False)
    buy_price = models.FloatField(null=False)
    description = models.CharField(null=False, max_length=500)
    product = models.CharField(null=False, max_length=100)
