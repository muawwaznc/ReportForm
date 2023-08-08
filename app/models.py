from django.db import models
from django.utils import timezone

class Muser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)

class ExtraNCPrograms(models.Model):
    name = models.CharField(max_length=100)

class NC(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    password = models.CharField(max_length=15)
    president = models.CharField(max_length=100)
    vicePresident = models.CharField(max_length=100, null = True, default="")
    secretory = models.CharField(max_length=100, null = True, default="")
    viceSecretory = models.CharField(max_length=100, null = True, default="")
    finance = models.CharField(max_length=100, null = True, default="")
    publicity = models.CharField(max_length=100, null = True, default="")
    womenContacts = models.CharField(max_length=100, null = True, default="")
    studyCircle = models.CharField(max_length=100, null = True, default="")
    youth = models.CharField(max_length=100, null = True, default="")
    politicalCouncil = models.CharField(max_length=100, null = True, default="")

class Report(models.Model):
    month = models.CharField(max_length=10)
    year = models.IntegerField()
    dawaProgramCount = models.IntegerField()
    extraProgramCount = models.IntegerField()
    NC = models.ForeignKey(NC, on_delete=models.CASCADE, related_name='reports')
     
class Block(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    president = models.CharField(max_length=100)
    secretory = models.CharField(max_length=100)
    NC = models.ForeignKey(NC, on_delete=models.CASCADE)

class ProgramsNC(models.Model):
    name = models.CharField(max_length=100)
    target = models.IntegerField()
    held = models.IntegerField()
    attendence = models.IntegerField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 
     
class LibraryNDawa(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    category = models.CharField(max_length=10)
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 

class Politics(models.Model):
    isPublicSecretariat = models.CharField(max_length=10)
    activity = models.TextField()
    tryOnCitizenIssue = models.TextField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 

class Alkhidmat(models.Model):
    isProject = models.CharField(max_length=10)
    isFutureProject = models.CharField(max_length=10)
    projectDetailsCount = models.IntegerField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 

class AlkhidmatProjectDetails(models.Model):
    detail = models.TextField()
    alkhidmat = models.ForeignKey(Alkhidmat, on_delete=models.CASCADE) 

class UpperProgram(models.Model):
    name = models.CharField(max_length=100)
    target = models.IntegerField()
    attendence = models.IntegerField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 
     
class IT(models.Model):
    facebook = models.CharField(max_length=100, default="No")
    whatsapp = models.CharField(max_length=15, default="No")
    email = models.CharField(max_length=100, default="No")
    youtube = models.CharField(max_length=100, default="No")
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 

class Finance(models.Model):
    name = models.CharField(max_length=100)
    previousBalance = models.IntegerField()
    amount = models.IntegerField()
    total = models.IntegerField()
    expenses = models.IntegerField()
    upper = models.IntegerField()
    currentBalance = models.IntegerField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 

class Arkan(models.Model):
    name = models.CharField(max_length=100)
    cetagory = models.CharField(max_length=10)
    rbt1 = models.CharField(max_length=100, default="")
    rbt2 = models.CharField(max_length=100, default="")
    rbt3 = models.CharField(max_length=100, default="")
    rbt4 = models.CharField(max_length=100, default="")
    rbt5 = models.CharField(max_length=100, default="")
    rbt6 = models.CharField(max_length=100, default="")
    NC = models.ForeignKey(NC, on_delete=models.CASCADE)

class Karkun(models.Model):
    name = models.CharField(max_length=100)
    NC = models.ForeignKey(NC, on_delete=models.CASCADE)

class Manpower(models.Model):
    arkanInitial = models.IntegerField()
    arkanAdded = models.IntegerField()
    arkanMinus = models.IntegerField()
    arkanNow = models.IntegerField()
    active = models.IntegerField()
    retired = models.IntegerField()
    passive = models.IntegerField()

    umeerwarInitial = models.IntegerField()
    umeerwarAdded = models.IntegerField()
    umeerwarMinus = models.IntegerField()
    umeerwarNow = models.IntegerField()

    arkanRwabit = models.IntegerField()
    arkanRwabitNumber = models.IntegerField()

    umeedwarRwabit = models.IntegerField()
    umeedwarRwabitNumber = models.IntegerField()

    karkun = models.IntegerField()
    voters = models.IntegerField()

    report = models.ForeignKey(Report, on_delete=models.CASCADE)

class NCYearlyReport(models.Model):
    sentence = models.CharField(max_length=20)
    start = models.IntegerField()
    goal = models.IntegerField()
    monthlyAdded = models.IntegerField()
    addedFromStart = models.IntegerField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

class NCGoals(models.Model):
    detail = models.TextField()
    NC = models.ForeignKey(NC, on_delete=models.CASCADE)