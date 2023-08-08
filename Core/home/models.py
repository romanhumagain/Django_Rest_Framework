from django.db import models

class Skill(models.Model):
  skill = models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return self.skill
  
class Department(models.Model):
  department = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.department
  
class Course(models.Model):
  course = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.course
  
  
class StudentInfo(models.Model):
  skill = models.ForeignKey(Skill , null=True , default=None, on_delete=models.ForeignKey)
  department = models.ForeignKey(Department ,null=True, default=None, on_delete=models.CASCADE)
  course = models.ForeignKey(Course ,null=True, default=None, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  
  def __str__(self) -> str:
    return self.name