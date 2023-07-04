from django.db import models

# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    travel_again = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# below Artist Model

class City(models.Model):

    name = models.CharField(max_length=150)
    population= models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="citys")

    def __str__(self):
        return self.name
    
    def get_population(self):
        number = format(self.population, ",")
        return number

class Favorite(models.Model):
    title = models.CharField(max_length=150)
    citys = models.ManyToManyField(City)

    def __str__(self):
        return self.title

