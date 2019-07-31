/* Get a column form a table*/ 
SELECT column name
FROM table name;

/* Get a few columns from a table */

SELECT column1, column2, column3
FROM table name;

/* Get all the columns in a table */

SELECT * 
FROM table name;

/* To get only uniqe vlaus from a column */

SELECT DISTINCT column
FROM table name;

/* to limit the number of row retrieved from a column*/

SELECT column
FROM table name
LIMIT 5;

/* Sorting Retrieved DATA */

/* Use Order By */

/* sort by on columnm */

SELECT column
FROM table name
ORDER BY  column; 

/* sort by multiple column*/

ELECT column1, column2, column3
FROM table name
ORDER BY  column1 , column3;

/* sort by direction */

SELECT column
FROM table name
ORDER BY  column [ASC|DESC];

/* ASC -down to up
   DESC - up to down
*/


/* Filtering DATA */

/* Use Where */

SELECT column
FROM table
WHERE condition
ORDER BY column [ASC|DESC]

/* For Example */

SELECT prod_name, prod_price
FROM Products
WHERE prod_price = 3.49;

/* filter using a range */

SELECT column1, column2 
FROM table
WHERE column BETWEEN 5 AND 10;


/*filter for no value*/

SELECT column1, column2 
FROM table
WHERE column IS NULL;

/* For Example */

SELECT cust_name
FROM Customers
WHERE cust_email is NULL;

/*Combine WHERE clauses*/

SELECT column1, column2 
FROM table
WHERE condition1  AND  condition2;

SELECT column1, column2 
FROM table
WHERE condition1  OR  condition2;

/* For Example */

SELECT prod_name, prod_price
FROM Products
WHERE vend_id = 'DLL01' 
AND prod_price <= 4;

/* For Example */


SELECT prod_name, prod_price
FROM Products
WHERE vend_id = 'DLL01' 
OR vend_id = 'BRS01';


/* Filter using IN */

SELECT prod_name, prod_price
FROM Products
WHERE vend_id IN ('DLL01', 'BRS01');

/* Negate using NOT */

SELECT prod_name, prod_price
FROM Products
WHERE NOT vend_id ='DLL01';


/*Filter using LIKE

% any number of caracters 
_ any single caracter 

[]%
*/
 
SELECT prod_name, prod_price
FROM Products
WHERE prod_name LIKE 'Fish%';


SELECT prod_name, prod_price
FROM Products
WHERE prod_name LIKE '%bean bag%';

SELECT prod_name, prod_price
FROM Products
WHERE prod_name LIKE '__inch teddy bear';


/* use alias */

SELECT vend_name || ' (' || vend_country || ') ' AS vend_title
FROM Vendors

/* perform mathematical calculation  */

SELECT prod_id, 
       quantity, 
	   item_price, 
	   quantity*item_price AS expaned_price
FROM OrderItems
WHERE order_num = 20008;



/* Summarizing DATA */

/* Avarge */

SELECT AVG(prod_price) AS avg_price
FROM Products;

/* Count */

SELECT COUNT(prod_price) AS count_price
FROM Products;

/* MAX */

SELECT MAX(prod_price) AS max_price
FROM Products;


/* MIN */

SELECT MIN(prod_price) AS max_price
FROM Products;

/* SUM */

SELECT SUM(prod_price) AS sum_price
FROM Products


/* Grouping  DATA */

/* Group BY */

SELECT vend_id, COUNT(*)  AS num_prods
FROM Products
GROUP BY vend_id;

/* Haveing  BY */

SELECT cust_id, COUNT(*)  AS orders
FROM Orders
GROUP BY cust_id
HAVING COUNT(*) >= 2;

/* Subqueries */

SELECT  cust_id
FROM Orders
WHERE order_num IN (SELECT order_num
                    FROM OrderItems
					WHERE prod_id = 'RGAN01');


/* Basic Join */

SELECT vend_name, prod_name, prod_price
FROM Vendors INNER JOIN Products
 ON Vendors.vend_id = Products.vend_id;



/* Join Multiple tables */

SELECT prod_name, vend_name, prod_price, quantity
FROM OrderItems, Products, Vendors
WHERE Products.vend_id = Vendors.vend_id
 AND OrderItems.prod_id = Products.prod_id
 AND order_num = 20007; 


/* Outer Join */

SELECT Customers.cust_id, Orders.order_num
FROM Customers LEFT OUTER JOIN Orders
 ON Customers.cust_id = Orders.cust_id;


/* Use Union ofr combaining queries */

SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL', 'IN', 'MI')
UNION
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4All';


/* Insert a row */

INSERT INTO Customers (cust_id,
   cust_name,
   cust_address,
   cust_city,
   cust_state,
   cust_zip,
   cust_country,
   cust_contact,
   cust_email)
 VALUES ('1000000006',
          'Toy Land',
		  '123 Any Street',
		  'New York',
		  'NY',
		  '11111',
		  'USA',
		  NULL,
		  NULL);

/* Insert retrieved data */

INSERT INTO Customers (cust_id,
   cust_name,
   cust_address,
   cust_city,
   cust_state,
   cust_zip,
   cust_country,
   cust_contact,
   cust_email)
 SELECT cust_id,
   cust_name,
   cust_address,
   cust_city,
   cust_state,
   cust_zip,
   cust_country,
   cust_contact,
   cust_email
 FROM CustNew;

/* Copy int another table */

SELECT *
INTO CustNew
From Customers;

/* Update a row */

UPDATE Customers
SET cust_email = 'kim@toystore.com'
WHERE cust_id = '1000000005';


/* Delete a row */

DELETE Customers
WHERE cust_id = '1000000005';