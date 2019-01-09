import urllib.request
import pymysql.cursors
"""
USE test;
DROP TABLE Exchanges;
CREATE TABLE Exchanges (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10),
    MuaTM FLOAT, 
    muaCK FLOAT, 
    ban FLOAT, 
    CONSTRAINT UC_Exchanges UNIQUE (name,MuaTM,muaCK,ban)
);
"""
class DatabaseManager:    
    instance = None
    def __init__(self):
        self.database = pymysql.connect(host="localhost",# your host, usually localhost
            user="root",         # your username
            passwd="",  # your password
            db="test",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)         
    def insert_into_exchanges(self, name, MuaTM, muaCK, ban):
        try:
            self.cursor = self.database.cursor()
            sql = "INSERT INTO Exchanges(name, MuaTM, muaCK, ban) VALUES('{}',{},{},{})".format(name, MuaTM, muaCK, ban)
            self.cursor.execute(sql)
            self.database.commit()
            print('Inserting values: {}, {}, {}, {} successfully'.format(name, MuaTM, muaCK, ban)) 
        except Exception as ex:
            if(ex.args[0] == 1062):
                pass
            print('Error inserting to Database: {}'.format(ex)) 
        finally:
            pass
    def get_instance():
        if DatabaseManager.instance is None:
            DatabaseManager.instance = DatabaseManager()
        return DatabaseManager.instance