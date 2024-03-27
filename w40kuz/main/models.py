from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    photo = models.ImageField('Картинка', upload_to='main\static\img')
    place = models.TextField('Ссылка', default='none')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Video(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Ссылка')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

class Photo(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Ссылка')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
