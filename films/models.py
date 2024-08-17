from django.db import models

class Posts(models.Model):
    title = models.CharField('Название фильма', max_length=80)
    synopsis = models.CharField('Синопсис', max_length=250, blank=True)
    review = models.TextField('Отзыв')
    pub_date = models.DateTimeField('Опубликовано', auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'