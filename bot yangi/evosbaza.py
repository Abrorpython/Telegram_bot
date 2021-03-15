import sqlite3
class ish:
    def __init__(self):
        self.con=sqlite3.connect("ish.db",check_same_thread=False)
        self.cur=self.con.cursor()
    def baza(self):
        self.cur.execute("""CREATE TABLE ish(
        user_id INTEGER,
        username  TEXT,
        ism TEXT,
        familya TEXT,
        age INTEGER,
        gender TEXT,
        yashash_manzili TEXT,
        user TEXT,
        user_tel INTEGER, 
        ish_malakasi INTEGER
        )""")
        self.con.commit()
        self.con.close()
    def info(self):
        self.cur.execute("""SELECT user_id FROM ish """)
        temp = self.cur.fetchall()
        l1 = []
        for i in temp:
            l1.append(i[0])
        return list(l1)
    def userid(self,id):
        self.cur.execute(f"""INSERT INTO ish (user_id) VALUES ({id})""")
        self.con.commit()
    def username(self,name,id):
        self.cur.execute(f"""UPDATE ish SET username="{name}" WHERE user_id={id} """)
        self.con.commit()
    def ism(self,name,id):
        self.cur.execute(f"""UPDATE ish SET ism="{name}" WHERE user_id={id}""")
        self.con.commit()
    def familya(self,surname,id):
        self.cur.execute(f"""UPDATE ish SET familya="{surname}" WHERE user_id={id}""")
        self.con.commit()
    def age(self,age,id):
        self.cur.execute(f"""UPDATE ish SET age={age} WHERE user_id={id}""")
        self.con.commit()
    def gender(self,gen,id):
        self.cur.execute(f"""UPDATE ish SET gender="{gen}" WHERE user_id={id}""")
        self.con.commit()
    def manzil(self,adres,id):
        self.cur.execute(f"""UPDATE ish SET yashash_manzili="{adres}" WHERE user_id={id}""")
        self.con.commit()
    def user(self,user2,id):
        self.cur.execute(f"""UPDATE ish SET user="{user2}" WHERE user_id={id}""")
        self.con.commit()
    def tel_nomer(self,tel,id):
        self.cur.execute(f"""UPDATE ish SET user_tel="{tel}" WHERE user_id={id}""")
        self.con.commit()
    def malaka(self,malaka,id):
        self.cur.execute(f"""UPDATE ish SET ish_malakasi={malaka} WHERE user_id={id}""")
        self.con.commit()

