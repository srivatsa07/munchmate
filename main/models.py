from django.db import models

class FoodSubmission(models.Model):
    foods = models.CharField(max_length=255)  # Or models.TextField() for longer input
    type = models.CharField(max_length=20)  # 'vegan', 'vegetarian', or 'other'
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.foods