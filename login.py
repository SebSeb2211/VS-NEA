import sqlite3





#DATABASE CREATION
def createDatabase():
    print("here")


    conn = sqlite3.connect('test.db')

#TABLE CREATION
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS subjects
                (id integer PRIMARY KEY AUTOINCREMENT, 
                subjectName varchar
                )''')
        print('Table created: subjects') 
    except Exception as e:
        print(e)

    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id integer PRIMARY KEY AUTOINCREMENT,
                username varchar
                )''')
        print('Table created: users')
    except Exception as e:
        print(e)

    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS userSubjects
                (id integer PRIMARY KEY AUTOINCREMENT,
                username varchar,
                subjectName varchar,
                FOREIGN KEY (username) REFERENCES users (username),
                FOREIGN KEY (subjectName) REFERENCES subjects (subjectName)
                )''')
        print('Table created: userSubjects')
    except Exception as e:
        print(e)

    
    conn.close()
    











#CLASS CREATION
class databaseInterface():

    def __init__(self):
        self.conn = sqlite3.connect('test.db')

#NEW SUBJECT
    def insertNewSubject(self, subjectName):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO subjects (subjectName) VALUES (?)",(subjectName,))
            self.conn.commit()
            #self.conn.close()
        
        except Exception as e:
            print(e)
#GET SUBJECTS
    def getAllSubjects(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM subjects")
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)


#SEARCH FOR SUBJECT BY NAME
    def getNamedSubject(self, subjectName):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM subjects WHERE subjectName = ?",(subjectName,))
            result = cursor.fetchone()
            return result

        except Exception as e:
            print(e)


#DELETE A SUBJECT
    def deleteSubject(self, subjectName):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM subjects WHERE subjectName = ?",(subjectName,))
        
        except Exception as e:
            print(e)


#NEW USER
    def insertNewUser(self, username):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (username) VALUES (?)",(username,))
            self.conn.commit()
        
        except Exception as e:
            print(e)


#GET USERS
    def getAllUsers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)


#GET NAMED USER
    def getNamedUser(self, username):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?",(username,))
            result = cursor.fetchone()
            return result

        except Exception as e:
            print(e)
    


#DELETE USER
    def deleteUser(self, username):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM users WHERE username = ?",(username,))
        
        except Exception as e:
            print(e)



#CREATE NEW USERSUBJECT
    def insertNewUserSubject(self, username, subjectName):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO userSubjects (username, subjectName) VALUES (?,?)",(username,subjectName))
            self.conn.commit()
        
        except Exception as e:
            print(e)





createDatabase()

dataB = databaseInterface()



# *** UP TO HERE ALREADY INCLUDED IN DB.PY *** #



login = False
while login == False:
    username = input("Username: ")
    searchName = dataB.getNamedUser(username)
    

    if username in searchName:
        print("Login successful")
        login = True

    else:
        print("Login unsuccessful")

print("Login sequence finished")


