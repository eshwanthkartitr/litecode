Select E.name as "Employee" from Employee As E Where E.id = Any(Select managerId from Employee)