"""
 @file: models.py
 @Time    : 2023/7/10
 @Author  : Peinuan qin
 """
from django.db import models
from django.db.models import JSONField


class Login(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # pwd = models.CharField(max_length=200)



class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Prompts(models.Model):
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person = models.CharField(max_length=200, unique=True)
    # prompts = models.CharField(max_length=1000)
    prompts = JSONField()
    # pub_date = models.DateTimeField('date published')




class ClickData(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    ProlificID = models.CharField(max_length=50, unique=True)
    condition = models.CharField(max_length=2000)
    main_task_1 = models.CharField(max_length=2000)
    edited_message_1 = models.CharField(max_length=2000)
    main_task_2 = models.CharField(max_length=2000)
    edited_message_2 = models.CharField(max_length=2000)
    main_task_3 = models.CharField(max_length=2000)
    edited_message_3 = models.CharField(max_length=2000)

class TaskOrder(models.Model):
    ProlificID = models.CharField(max_length=50, unique=True)
    current = models.CharField(max_length=10)
    order1 = models.CharField(max_length=10)
    order2 = models.CharField(max_length=10)
    order3 = models.CharField(max_length=10)

class Training(models.Model):
    ProlificID = models.CharField(max_length=50, unique=True)
    training_1 = models.CharField(max_length=2000)
    training_2 = models.CharField(max_length=2000)
    training_3 = models.CharField(max_length=2000)

class ExperienceAndAttitude(models.Model):
    ProlificID = models.CharField(max_length=50, unique=True)
    experience_1 = models.CharField(max_length=2000,null=True)
    thought_1 = models.CharField(max_length=2000,null=True)
    experience_2 = models.CharField(max_length=2000,null=True)
    thought_2 = models.CharField(max_length=2000,null=True)
    experience_3 = models.CharField(max_length=2000,null=True)
    thought_3 = models.CharField(max_length=2000,null=True)
    
    

class Time(models.Model):
    pid = models.CharField(max_length=100, unique=True)
    training_start_1 = models.CharField(max_length=20,null=True)
    training_start_2 = models.CharField(max_length=20,null=True)
    training_start_3 = models.CharField(max_length=20,null=True)
    training_end_1 = models.CharField(max_length=20,null=True)	
    training_end_2 = models.CharField(max_length=20,null=True)
    training_end_3 = models.CharField(max_length=20,null=True)
    question_start_1 = models.CharField(max_length=20,null=True)
    question_start_2 = models.CharField(max_length=20,null=True)
    question_start_3 = models.CharField(max_length=20,null=True)
    question_end_1 = models.CharField(max_length=20,null=True)	
    question_end_2 = models.CharField(max_length=20,null=True)
    question_end_3 = models.CharField(max_length=20,null=True)
    main_task_start_1 = models.CharField(max_length=20)
    main_task_start_2 = models.CharField(max_length=20)
    main_task_start_3 = models.CharField(max_length=20)
    main_task_end_1 = models.CharField(max_length=20)
    main_task_end_2 = models.CharField(max_length=20)
    main_task_end_3 = models.CharField(max_length=20)
    editing_start_1 = models.CharField(max_length=20,null=True)
    editing_start_2 = models.CharField(max_length=20,null=True)
    editing_start_3 = models.CharField(max_length=20,null=True)
    editing_end_1 = models.CharField(max_length=20,null=True)
    editing_end_2 = models.CharField(max_length=20,null=True)
    editing_end_3 = models.CharField(max_length=20,null=True)



