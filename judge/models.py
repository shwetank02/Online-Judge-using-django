from django.db import models

class problem(models.Model):
    name=models.TextField()
    statement = models.TextField()
    difficulty=models.TextField()


class solution(models.Model):
    curr_problem=models.ForeignKey(problem, on_delete=models.CASCADE, null=True)
    verdict=models.TextField(default='WA')
    time_of_submit = models.DateTimeField(auto_now=True)
    code=models.TextField(null=True, blank=True)
    

class testcase(models.Model):
    curr_problem=models.ForeignKey(problem, on_delete=models.CASCADE)
    input=models.TextField()
    output=models.TextField()
