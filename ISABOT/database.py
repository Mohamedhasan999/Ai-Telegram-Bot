import sqlite3



class data:

    def __init__(self, db_name="chtbot.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age TEXT NOT NULL,
                country TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                major TEXT NOT NULL,
                graduation_year TEXT NOT NULL,
                job TEXT NOT NULL

            )
        ''')
        self.conn.commit()

    def add_user(self, name, age, country, phone, email, major, graduation_year, job):
        self.db_name = "chtbot.db"
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        read= self.cursor.execute('SELECT * FROM users WHERE (name,phone) = (?,?)',(name, phone))
        if read.fetchone() is not None:
            print("تم تسجيل البيانات بنجاح")
        else:    
         self.cursor.execute('''
            INSERT INTO users (name, age, country, phone, email, major, graduation_year, job) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, age, country, phone, email, major, graduation_year, job))
        
        
        self.conn.commit()
        self.conn.close()

    # def get_users(self):
    #     self.cursor.execute('SELECT * FROM users')
    #     return self.cursor.fetchall()

