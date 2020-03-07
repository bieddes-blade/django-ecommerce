# django-ecommerce

Postman:\ https://www.getpostman.com/collections/f0870325551a41616843

Main requests:\
GET 127.0.0.1:8000/products/ - lists all products\
GET 127.0.0.1:8000/products/1/ - shows product by id\
POST 127.0.0.1:8000/products/ with content-type: application/json and data: {"name":"shoes","code":"JS001","categ":2} - creates a new product

Other requests:\ OPTIONS (127.0.0.1:8000/products/), PUT, DELETE (127.0.0.1:8000/products/1/)
