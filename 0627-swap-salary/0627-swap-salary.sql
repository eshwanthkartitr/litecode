Update Salary
Set sex=CASE
    When sex='f' then 'm'
    When sex='m' then 'f'
End;