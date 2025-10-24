from django.db import models
from django.core.validators import RegexValidator

class Application(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+79991234567'."
    )
    
    phone = models.CharField(
        'Номер телефона',
        max_length=16,
        validators=[phone_regex]
    )
    
    email = models.EmailField('Email', max_length=100)
    message = models.TextField('Текст обращения', max_length=500)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заявка #{self.id} от {self.phone}'