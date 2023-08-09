from django.db import models

# Create your models here.
class Person_Skill(models.Model):
  skill = models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return self.skill
  
class Person(models.Model):
  skill = models.ForeignKey(Person_Skill,null=True, on_delete=models.CASCADE , related_name='person_skill')
  name = models.CharField(max_length=100)
  age = models.IntegerField(null=True, default=None)
  address = models.CharField(max_length=100)
  contact = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.name
