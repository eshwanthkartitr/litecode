select Distinct v2.author_id as id from Views as v1
Join Views as v2 On v1.author_id = v2.viewer_id
Order by v2.author_id