from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.http import JsonResponse

try:
    df = pd.read_excel("Dummy Employee Data.xlsx")
    df.sort_values("Employee ID")
except FileNotFoundError:
    df = pd.DataFrame()

employee_data = df.to_json()

def getEmployee(emp_id):
    for row in employee_data:
        try:
            if row['Employee ID']==emp_id:
                return row
        except KeyError:
            return False
    return False

@login_required
def get_all_employees(request):
    if request.method=="GET":
        return JsonResponse({"data": employee_data}, status=200)
    else:
        return JsonResponse({"message": "Not allowed"}, status=403)

@login_required
def get_employee_info(request):
    if request.method=="GET":
        emp_id = request.GET.get("emp_id")
        if not emp_id:
            return JsonResponse({"message": "emp_id required"}, status=400)
        response_data = getEmployee(emp_id)        
        if not response_data:
            return JsonResponse({"message": "Employee information not found"}, status=404)
        return JsonResponse({"data": response_data}, status=200)
    return JsonResponse({"message": "Not allowed"}, status=403)