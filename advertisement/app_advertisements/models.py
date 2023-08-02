from django.db import models
from django.contrib import admin
from django.utils.html import format_html


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

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%y')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', updated_time
             )
        return self.update_at.strftime('%d.%m.%y')



