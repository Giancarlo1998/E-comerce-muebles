from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


# Product Model
class Product(models.Model):
    nombre = models.CharField(max_length=300)
    categoria = models.ForeignKey(Category,  on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='products/')
    videojc = models.FileField(upload_to='products/', null=True, blank=True, verbose_name='Video')
    detail = models.TextField(max_length=300, verbose_name='Información del producto')
    dimensiones = models.TextField(max_length=150, verbose_name='Dimensiones')
    materiales = models.TextField(max_length=150, verbose_name='Materiales')
    marked_price = models.PositiveIntegerField(null=True, blank=True, verbose_name='Precio Original')
    price = models.IntegerField()
    warranty = models.CharField(max_length=300, null=True, blank=True, verbose_name='¿Garantia?')
    linkjc = models.CharField(max_length=300, null=True, blank=True, verbose_name='URL')
    view_count = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="products/images/")
'''
    def __str__(self):
        return self.product.title
'''