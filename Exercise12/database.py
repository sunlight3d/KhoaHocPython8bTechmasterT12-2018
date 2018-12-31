# pip3 install mysql-connector-python
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
            print('Connect to databse failed. Error = {}'.format(error))        

    """List all products"""
    def get_all_products(self, text=''):
        if (text.strip() == ''):
            self.cursor.execute("SELECT * FROM Products WHERE name like '%{}%' OR company like '%{}%'".format(text, text))
        else:
            self.cursor.execute("SELECT * FROM Products limit 20")
        products = []
        for (name, year, company, category) in self.cursor:
            products.append({"name": name, "year": year, "company": company, "category": category})
        return products

    def insert_new_product(self,name,year,company,category):
        try:
            self.cursor.execute("INSERT INTO Products"
                                "(name, year, company, category) "
                                "VALUES(%s, %d, %s, %s)", (name,year,company,category))
            product_id = self.cursor.lastrowid
            self.connection.commit()            
            return product_id
        except Exception as error:            
            return -1        
    
    def update_product(self,product_id, name,year,company,category):
        try:
            update_values = []
            if(name):
                update_values.append("name='{}'".format(name))
            if(year):
                update_values.append("year='{}'".format(year))
            if(company):
                update_values.append("company='{}'".format(company))
            if(category):
                update_values.append("category='{}'".format(category))                    
            self.cursor.execute("UPDATE Products SET "+','.join(update_values)+
                                " VALUES(%s, %s, %s, %s)", (name,year,company,category))            
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
    
    def check_login(self, email='', password=''):
        self.cursor.execute("SELECT * FROM Users WHERE email=%s AND password=%s", (email, password))
        if len(self.cursor.fetchall()) > 0:
            return True
        return False