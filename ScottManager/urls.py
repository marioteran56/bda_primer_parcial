from django.urls import path
from .views import DeptView, EmpView, NoEmpDeptView

urlpatterns = [
    path('departments/', DeptView.as_view(), name='departments_list'),
    path('departments/<int:deptno>', DeptView.as_view(), name='departments_process'),
    path('departments/<int:deptno>/employees', NoEmpDeptView.as_view(), name='departments_employees'),
    path('employees/', EmpView.as_view(), name='employees_list'),
    path('employees/<int:empno>', EmpView.as_view(), name='employees_process')
]
