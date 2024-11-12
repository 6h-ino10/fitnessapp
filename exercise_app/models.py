from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
import json

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
    description = models.TextField(max_length=200,blank=True)
    category = models.CharField(max_length=10,choices=EXERCISE_CATEGORY)
    difficulty_level = models.CharField(max_length=10,choices=DIFFICULTY_LEVEL)
    calories_burned = models.IntegerField(default=0)
    video_url = models.URLField(blank=True)

    exercise_id = models.CharField(max_length=100,unique=True)
    gif_url = models.URLField(blank=True)
    instructions = models.TextField(blank=True)
    target_muscled = models.TextField(blank=True)
    body_parts = models.TextField(blank=True)
    equipments = models.TextField(blank=True)
    secondary_muscles = models.TextField(blank=True)

    def set_instructions(self,instructions_list):
        self.instructions = json.dumps(instructions_list)

    def get_instructions(self):
        return json.loads(self.instructions)
    
    def set_target_muscles(self,muscles_list):
        self.target_muscles = json.dumps(muscles_list)

    def get_target_muscles(self):
        return json.loads(self.target_muscles)
    
    def set_body_parts(self,body_parts_list):
        self.body_parts = json.dumps(body_parts_list)

    def get_body_parts(self):
        return json.loads(self.body_parts)
    
    def set_equipments(self,equipments_list):
        self.equipments = json.dumps(equipments_list)

    def get_equipments(self):
        return json.loads(self.equipments)
    
    def set_secondary_muscles(self,muscles_list):
        self.secondary_muscles = json.dumps(muscles_list)

    def get_secondary_muscles(self):
        return json.loads(self.secondary_muscles)

    def __str__(self):
        return self.name
