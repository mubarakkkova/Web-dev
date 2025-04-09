from django.db import models
from pydoc import describe

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='None')
    city = models.CharField(max_length=255)
    address = models.TextField(default='Almaty')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description' : self.description,
            'city' : self.city,
            'address' : self.address
        }
    
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='None')
    salary = models.FloatField(default=1000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='vacancies')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary' : self.salary,
        }

