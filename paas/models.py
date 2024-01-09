from django.db import models
from accounts.models import Organization

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)

class Framework(models.Model):
    name = models.CharField(max_length=200)

class DeploymentPlan(models.Model):
    type =(
        ('Starter', 'Starter'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    )

    storage = models.IntegerField()
    bandwidth = models.IntegerField()
    memory = models.IntegerField()
    cpu = models.IntegerField()
    monthly_cost = models.FloatField()
    hourly_cost = models.FloatField()

#Specification for App
class App(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.ProtectedError)
    framework = models.ForeignKey(Framework, on_delete=models.ProtectedError)
    deployment_plan_type = models.ForeignKey(DeploymentPlan, on_delete=models.ProtectedError)


class DatabasePlan(models.Model):
    type =(
        ('Starter', 'Starter'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    )

    storage = models.IntegerField()
    bandwidth = models.IntegerField()
    memory = models.IntegerField()
    cpu = models.IntegerField()
    monthly_cost = models.FloatField()
    hourly_cost = models.FloatField()

#Database Specification
class Database(models.Model):
    TYPE = (
        ('Standard', 'Standard'),
        ('Nearline', 'Nearline'),
        ('Coldline', 'Coldline'),
    )
    type = models.CharField(max_length=200, choices=TYPE)
    database_plan = models.ForeignKey(DatabasePlan, on_delete=models.ProtectedError)


#Final App Deployment
class AppDeployment(models.Model):
    user = models.ForeignKey(Organization, on_delete=models.ProtectedError)
    github_repo = models.URLField()
    github_branch = models.URLField()

    app = models.ForeignKey(App, on_delete=models.ProtectedError)
    database = models.ForeignKey(Database, on_delete=models.ProtectedError)

#Environment Variable for each app deployment
class EnvVariables(models.Model):
    app = models.ForeignKey(AppDeployment, on_delete=models.ProtectedError)
    key = models.CharField(max_length=100)
    value = models.URLField()