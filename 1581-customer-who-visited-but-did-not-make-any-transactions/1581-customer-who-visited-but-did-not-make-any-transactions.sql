Select V.customer_id,count(*) as count_no_trans  from Visits as V
left Join Transactions as T on T.visit_id = V.visit_id
where T.amount is Null
Group by V.customer_id