from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Exercise(models.Model):
    EXERCISE_CATEGORY = [
        ("上半身","上半身"),
        ("下半身","下半身"),
        ("腹部","腹部"),
        ("二の腕","二の腕"),
        ("太もも","太もも"),
    ]

    DIFFICULTY_LEVEL = [
        ("初級","初級"),
        ("中級","中級"),
        ("上級","上級"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=10,choices=EXERCISE_CATEGORY)
    difficulty_level = models.CharField(max_length=10,choices=DIFFICULTY_LEVEL)
    calories_burned = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(1000)])
    video_url = models.URLField()

    def __str__(self):
        return self.name
