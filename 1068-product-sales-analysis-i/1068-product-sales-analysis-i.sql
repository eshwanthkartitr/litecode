Select p1.product_name,s1.year,s1.price from Sales as s1
Inner Join Product as p1 On p1.product_id=s1.product_id