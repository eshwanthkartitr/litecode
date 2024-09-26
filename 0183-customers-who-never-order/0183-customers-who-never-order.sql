Select name As "Customers" from Customers Where id != ALL
(Select C.id from Customers AS C
JOIN Orders as O ON C.id = O.customerId)