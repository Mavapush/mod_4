from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):

    title = models.CharField("Заголовок", max_length=120)


    description = models.TextField("описание")


    price = models.DecimalField("цена",max_digits=10, decimal_places=2)


    auction = models.BooleanField("Торг" , help_text="отметьте если хотите торговаться")


    created_at = models.DateTimeField(auto_now_add=True)


    updated_at = models.DateTimeField(auto_now=True)    
    
    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        
        if self.created_at.date() == timezone.now().date():
            created_time= self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
            return format_html("<span style='color:green;font-weight:bold'> сегодня в {}</span>",created_time)


        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'