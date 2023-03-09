
CREATE DATABASE online_store;

CREATE TABLE products(
	products_id int PRIMARY KEY , 
	product_name varchar(255) NOT NULL, 
	decription TEXT, 
	price int NOT NULL ,
	units_in_stock int NOT NULL 
);

CREATE TABLE customers(
	customer_id int PRIMARY KEY ,
	full_name varchar(128) NOT NULL ,
	customer_mail varchar(128),
	customer_password varchar(128) NOT NULL 
	
);

CREATE TABLE orders(
	order_id int PRIMARY KEY, 
	customer_id int NOT NULL, 
	order_date DATA NOT NULL, 
	total_price decimal(10,2) NOT NULL ,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


CREATE TABLE order_items (
  order_id int NOT NULL,
  product_id int NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(products_id)
  
);

