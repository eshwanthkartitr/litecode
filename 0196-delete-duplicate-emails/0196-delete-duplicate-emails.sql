DELETE FROM Person p1 USING Person p2
Where p1.id > p2.id and p1.email = p2.email