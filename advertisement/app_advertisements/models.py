from django.db import models


class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)    # (CharField - аналог str в python)
    description = models.TextField('Описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)   # числовое поле
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction= models.BooleanField('торг', help_text='Отметьте, если уместен торг')

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"



