import sqlite3
import pathlib
import datetime

class data:
    def __init__(self):
        #database = str(pathlib.Path().absolute())+"\cobapbo.db"
        self.connector = sqlite3.connect(r"C:\Users\Dimas Yudhistira\Documents\yDhiz\sofi\kasir.db")
        self.cursor = self.connector.cursor()

    def executeQuery(self, query, retval=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.connector.commit()
        if retval:
            return all_results

class pengguna(data):

    def __init__(self):
        data.__init__(self)
        self.user_id = None
        self.username = None
        self.password = None

    def masuk(self, username, password):
        query = 'SELECT user_id, username, password FROM data_user \
            where username=\'%s\' and password=\'%s\''
        query = query % (username, password)
        masuk = self.executeQuery(query, True)
        status = False

        for i in range(0,len(masuk)):
            if username == masuk[i][1] and password == masuk[i][2]:
                status = True
                self.user_id = masuk[i][0]
                self.username = masuk[i][1]
                self.password = masuk[i][2]
                print("berhasil masuk!")
                print(f"selamat datang {self.username}")
        if status == False:
            print("Data tidak ditemukan")
    
    def daftar(self, username, password):
        query = 'INSERT INTO data_user (username, password) \
            VALUES (\'%s\', \'%s\')'
        query = query % (username, password)
        self.executeQuery(query)
        query = 'SELECT user_id, username, password FROM data_user where username=\'%s\' and password=\'%s\' '
        query = query % (username, password)
        masuk = self.executeQuery(query, True)

        for i in range(0, len(masuk)):
            if username == masuk[i][1] and password == masuk[i][2]:
                self.user_id = masuk[i][0]
            self.username
            self.password
            print("Akun berhasil dibuat!")
    def fungsimakanan(self, nomormakanan, porsi):
        total1 = 0
        if nomormakanan==1:
            total1=porsi*10000
            print (porsi," French Fries = Rp", total1)
            jenis1=("French Fries")
        elif nomormakanan==2:
            total1=porsi*13000
            print (porsi," Panna Cotta = Rp", total1)
            jenis1=("Panna Cotta")
        elif nomormakanan==3:
            total1=porsi*18000
            print (porsi, " Beef Cheese Burger = Rp", total1)
            jenis1=("Beef Chesse Burger")
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!")
            
        return total1
    def menumakanan(self):
        print ("\n~~~~Menu Makanan~~~~")
        print("1. French Fries       - Rp10000")
        print("2. Panna Cotta        - Rp12500")
        print("3. Beef Chesse Burger - Rp18000")
    def fungsiminuman(self, nomorminuman, gelas):
        total2 = 0
        if nomorminuman==1:
            total2=gelas*8000
            print (gelas," Espresso = Rp", total2)
            jenis2=("Espresso")
        elif nomorminuman==2:
            total2=gelas*10000
            print (gelas, "Coffee Milk ice = Rp", total2)
            jenis2=("Coffee Milk Ice")
        elif nomorminuman==3:
            total2=gelas*15000
            print (gelas, " Caramel Machiatto = Rp", total2)
            jenis2=("Caramel Machiatto")
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!")
            
        return total2
    def menuminuman(self):
        print("\n~~~~Menu Minuman~~~~")
        print("1. Espresso               - Rp8000")
        print("2. Coffee Milk Ice        - Rp10000")
        print("3. Tiramisu Coffee Cream  - Rp13000")
        print("4. Caramel Machiatto      - Rp15000")

u = pengguna()
while True:
    print('''
    1. login
    2. register
    3. pilih menu
    4. checkout
    5. exit program''')
    menu = input()
    
    if menu == "1":
        username = str(input("Masukan Username: "))
        password = str(input("Masukan Password: "))
        u.masuk(username, password)
    
    elif menu == "2":
        username = str(input("Masukan Username: "))
        password = str(input("Masukan Password: "))
        u.daftar(username, password)
    
    elif menu == "3":
        if u.username == None:
            print("silahkan Login / Register terlebih dahulu")
        else :
            u.menumakanan()
            u.menuminuman()
            nomormakanan=int(input("Masukan Pilihan: "))
            porsi= int(input("Berapa Porsi: "))
            nomorminuman=int(input("Masukan Pilihan: "))
            gelas= int(input("Berapa Gelas: "))
            total1 =  u.fungsimakanan(nomormakanan, porsi)
            total2 = u.fungsiminuman(nomorminuman, gelas)
            total = total1+total2
            print(total)
            uang_pembeli = int(input("Uang Pembeli : "))

    elif menu == "4":
        kembalian = uang_pembeli - total
        print("Kembalian : ",kembalian)