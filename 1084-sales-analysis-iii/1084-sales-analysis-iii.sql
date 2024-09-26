Select product_id,product_name from Product
Where product_id not in (Select p1.product_id from Product as p1
Inner Join Sales as s1 On s1.product_id=p1.product_id 
Where '2019-01-01' > s1.sale_date or s1.sale_date > '2019-03-31')