from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductModelTest(TestCase):
    
    def test_create_product(self):
        
        product = Product.objects.create(
            nome="Notebook Gamer",
            descricao="Notbook com RTX 4090",
            preco=15000.00
        )

        
        self.assertEqual(Product.objects.count(), 1)
        
        
        self.assertEqual(product.nome, "Notebook Gamer")
        self.assertEqual(product.descricao, "Notbook com RTX 4090")
        self.assertEqual(float(product.preco), 15000.00)

class ProductListViewTest(TestCase):
    
    def test_product_list_status_code(self):
        
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)  
 
