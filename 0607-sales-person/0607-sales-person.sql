Select name From SalesPerson
Where sales_id not in (
Select o1.sales_id From Orders as o1
Join Company as c1 on c1.com_id = o1.com_id 
where c1.name = 'RED'    
)