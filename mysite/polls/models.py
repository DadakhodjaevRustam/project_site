from django.db import models



class Product(models.Model):
    """
    Сущность продукта.
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField('Название',max_length=255)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
class Access(models.Model):
    """
    Сущность доступа к продукту.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user} has access to {self.product}"

    class Meta:
        verbose_name = 'Доступ к продукту'
        verbose_name_plural = 'Доступ к продуктам'
class Lesson(models.Model):
    """
    Сущность урока.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
class Group(models.Model):
    """
    Сущность группы.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_users = models.IntegerField()
    max_users = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
class GroupUser(models.Model):
    """
    Связь между группами и пользователями.
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Связь группы и пользователя'
        verbose_name_plural = 'Связи группы и пользователя'