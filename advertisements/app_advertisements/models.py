from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если будет уместен торг")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="advertisements/")

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; forn-weight: bold">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description="Дата редактирования")
    def up_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: #008080; forn-weight: bold">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Изображение')
    def image_py(self): 
        from django.utils.html import format_html
        if self.image:
            return format_html(
                '<a href="{0}" target="_blank"><img src="{0}" width="35"/></a>', self.image.url
            )
        else:
            return '(Нет изображения)'

    def __str__(self):
        return f'{[self.title, self.description, self.price, self.auction, self.created_at, self.updated_at]!r}'
    
    class Meta:
        db_table = '"advertisements"'