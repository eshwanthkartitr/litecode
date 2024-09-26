Select p1.project_id,Round(Avg(e1.experience_years),2) as "average_years" from Project as p1
Inner join Employee as e1 On p1.employee_id = e1.employee_id
Group by p1.project_id