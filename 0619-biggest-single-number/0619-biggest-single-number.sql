Select Max(num) as "num" from MyNumbers
Where num not in (
Select num from MyNumbers
Group by num
having count(num) > 1)