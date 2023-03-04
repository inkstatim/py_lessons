SELECT c.company_name,concat(e.first_name,'', e.last_name) 
FROM orders o
JOIN customers c USING(customer_id)
JOIN employees e USING(employee_id)
JOIN shippers s ON o.ship_via = s.shipper_id 
WHERE c.city = 'London' AND e.city = 'London' AND s.company_name ='Speedy Express';

SELECT product_name, units_in_stock, contact_name, phone
FROM products p 
JOIN categories c USING(category_id )
JOIN suppliers s USING(supplier_id)
WHERE category_name IN ('Beverages','Seafood') AND discontinued = 0 AND units_in_stock < 20
ORDER BY units_in_stock   ;

SELECT contact_name , order_id
FROM customers c
LEFT JOIN orders o  using(customer_id)
WHERE order_id IS NULL ;

SELECT contact_name , order_id
FROM orders c
RIGHT JOIN customers o using(customer_id)
WHERE order_id IS NULL 

