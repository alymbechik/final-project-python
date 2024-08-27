from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Food(models.Model):
    title = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/food_images')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12)



    def __str__(self):
        return f'{self.category} / {self.title}'

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class Lead(models.Model):
    name = models.CharField(max_length=123)
    subject = models.CharField(max_length=123)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'