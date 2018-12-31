# pip3 install mysql-connector-python
"""
DROP TABLE pythontutorial.users;
CREATE TABLE IF NOT EXISTS pythontutorial.users (
            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            email VARCHAR(50),
            password VARCHAR(50),
            created_date TIMESTAMP);
INSERT INTO pythontutorial.users(name,email,password) VALUES('Hoang', 'hoang123@gmail.com', '123456');
SELECT * FROM pythontutorial.users;

DROP TABLE pythontutorial.products;
CREATE TABLE IF NOT EXISTS pythontutorial.products (
            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            year INT(5)  NOT NULL,
            company VARCHAR(50),
            category VARCHAR(50) NOT NULL,
            user_id INT(6),            
            created_date TIMESTAMP);
INSERT INTO pythontutorial.products(name,year,company,category, user_id) VALUES('iphone X Red', 2017, 'Apple', 'Technology', 1);
SELECT * FROM pythontutorial.products;
"""

import mysql.connector

class Database:
    __instance = None

    @staticmethod 
    def getInstance():      
        if Database.__instance is None:
            Database.__instance = Database()
        return Database.__instance
    def __init__(self):
        self.server_name = 'localhost'
        self.database_name = 'pythontutorial'
        self.user_name = 'root'
        self.password = ''        
        try:
            self.connection = mysql.connector.connect(user=self.user_name, 
                                password=self.password,
                                  host=self.server_name,
                                  database=self.database_name)
            self.cursor = self.connection.cursor()
            print('Connect database successfully')                  
        except mysql.connector.Error as error:                                    
            print('Connect to database failed. Error = {}'.format(error))        

    """List all products"""
    def get_all_products(self, text=''):
        if (text.strip() == ''):
            self.cursor.execute("SELECT * FROM Products WHERE name like '%{}%' OR company like '%{}%'".format(text, text))
        else:
            self.cursor.execute("SELECT * FROM Products limit 20")
        products = []
        for (id,name, year, company, category, user_id, created_date) in self.cursor:
            products.append({"id": id, "name": name, "year": year, "company": company, "category": category})
        return products

    def get_product_from_id(self, product_id):
        self.cursor.execute("SELECT * FROM Products WHERE id=?",(product_id))
        return self.cursor[-1]
    def insert_new_product(self,new_product):                
        try:
            self.cursor.execute("INSERT INTO Products"
                                "(name, year, company, category) "
                                "VALUES(%s, %d, %s, %s)", (new_product['name'],new_product['year'],new_product['company'],new_product['category']))
            product_id = self.cursor.lastrowid
            self.connection.commit()            
            return product_id
        except Exception as error:            
            return -1
           
    
    def update_product(self,product_id, new_product):
        name = new_product['name']
        year = new_product['year']
        company = new_product['company']
        category = new_product['category']
        update_values = []
        try:            
            if(name):
                update_values.append("name='{}'".format(name))
            if(year):
                update_values.append("year='{}'".format(year))
            if(company):
                update_values.append("company='{}'".format(company))
            if(category):
                update_values.append("category='{}'".format(category))                    
            sql = "UPDATE Products SET "+','.join(update_values)+" WHERE id={}".format(product_id)
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as error:            
            return False   
    def delete_product(self,product_id):
        try:
            self.cursor.execute("DELETE Products"
                                " WHERE id=%s", (product_id))            
            self.connection.commit()            
            return True
        except Exception as error:            
            return False 
    
    def login(self, email='', password=''):
        self.cursor.execute("SELECT * FROM Users WHERE email=%s AND password=%s", (email, password))
        for (id,name, year, company, category, user_id, created_date) in self.cursor:
            return {"id": id, "name": name, "year": year, "company": company, "category": category}
        return None        