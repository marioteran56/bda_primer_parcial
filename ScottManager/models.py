from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=14)
    loc = models.CharField(max_length=13)
    
    class Meta:
        managed = False
        db_table = 'dept'
        
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=9)
    mgr = models.ForeignKey('self', models.DO_NOTHING, db_column='mgr', blank=True, null=True)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    comm = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='deptno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp'