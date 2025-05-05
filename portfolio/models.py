from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/images')
    category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)
    url = models.URLField(default='https://github.com/Xodikulov?tab=repositories')
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=70)
    size = models.CharField(max_length=20, default='col-lg-5')

    def __str__(self):
        return f"{self.title} by {self.category}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
