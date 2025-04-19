from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length = 100, unique = True, verbose_name = 'Название')
    slug = models.SlugField(max_length = 120, unique=True, blank = True, null = True, verbose_name='url')
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Products(models.Model):
      name = models.CharField(max_length = 100, unique = True, verbose_name = 'Название')
      slug = models.SlugField(max_length = 120, unique=True, blank = True, null = True, verbose_name='url')
      description = models.TextField(max_length=200, blank=True,null=True, verbose_name='Описание товара')
      image = models.ImageField(upload_to = 'images_product', blank=True,null=True, verbose_name='Изображение')
      price = models.DecimalField(default =0.00, max_digits = 7, decimal_places =2, verbose_name='Цена')
      discount=models.DecimalField(default =0.00, max_digits = 7, decimal_places =2, verbose_name='Скидка в %')
      quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
      category=models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
      
      def __str__(self):
        return self.name
        
      db_table = 'product'
      verbose_name = 'Продукт'
      verbose_name_plural = 'Продукты'
      def __str__(self):
        return f'{self.name} {self.quantity}'

      def display_id(self):
        return f'{self.id:04}'

      def sell_price(self):
        if self.discount:
          return round (self.price - self.price * self.discount / 100, 2)
        else:
          return self.price
