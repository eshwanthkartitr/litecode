Select * from Cinema
Where description != 'boring' and mod(id,2)!=0
Order by rating
Desc