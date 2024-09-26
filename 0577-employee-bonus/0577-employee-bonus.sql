Select e1.name,o1.bonus From Employee as e1
Left Outer Join Bonus as o1
On e1.empId = o1.empId
Where o1.bonus < 1000 or o1.bonus is null