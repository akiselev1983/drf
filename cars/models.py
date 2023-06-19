from django.db import models

"""
Створити модель Car з такими полями:
- марка машини
- рік випуску
- кількість місць
- тип кузову
- об'єм двигуна (float)

реалізувати всі CRUD операції
при виведені всіх машин показувати тільки (id, марку машини та рік)
"""
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seat_count = models.IntegerField()
    body_type = models.CharField(max_length=25)
    engine_volume = models.FloatField()
