import os 

def daftar() : 
    print("""
1. balok 
2. kubus 
3. tabung 
4. bola 
5. limas  
""")

#header utama 
def header():
    '''fungsi Header'''
    
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}\n")

#header bbalok 
def header_balok():
    '''fungsi Header'''
    
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG':^40}")
    print(f"{'RUMUS RUMUS BANGUN RUANG BALOK ':^40}")
    print(f"{'-'*40:^40}\n")
#header kubus 
def header_KUBUS():
    '''fungsi Header'''
    
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG':^40}")
    print(f"{'RUMUS RUMUS BANGUN RUANG KUBUS ':^40}")
    print(f"{'-'*40:^40}\n")
#HEADER TABUNG
def header_TABUNG():
    '''fungsi Header'''
    
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG':^40}")
    print(f"{'RUMUS RUMUS BANGUN RUANG TABUNG ':^40}")
    print(f"{'-'*40:^40}\n")
def header_BOLA():
    '''fungsi Header'''
    
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG':^40}")
    print(f"{'RUMUS RUMUS BANGUN RUANG BOLA ':^40}")
    print(f"{'-'*40:^40}\n")
def header_Kerucut():
    '''fungsi Header'''
    
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG':^40}")
    print(f"{'RUMUS RUMUS BANGUN RUANG KERUCUT ':^40}")
    print(f"{'-'*40:^40}\n")


#------------------------------------------------------------------------------

#BALOK 
def input_pertama_balok (): 
    panjang = float(input("Masukan panjang balok   = "))
    lebar = float(input("Masukan lebar balok       = "))
    tinggi = float(input("Masukan tinggi balok  = "))
    return panjang,lebar,tinggi

def volume(panjang,lebar,tinggi) : 
    volume = float(panjang*lebar*tinggi)
    return volume 
def luas_permukaan (panjang,lebar,tinggi) : 
    luas = 2 * (panjang*lebar + lebar*tinggi + panjang*tinggi)
    return luas 
def keliling(panjang,lebar,tinggi): 
    keliling = 4 * (panjang+lebar+tinggi)
    return keliling 
def diagonal_ruang(panjang,lebar,tinggi) : 
    diagonalbalok = (panjang**2 + lebar**2 + tinggi**2)**0.5
    return diagonalbalok

#--------------------------------------------------------------------------------

#kubus
def volume_kubus(sisi) : 
    v = sisi*sisi*sisi
    return v
def luas_kubus(sisi):
    L = 6*(sisi*sisi)
    return L
def keliling_kubus(sisi):
    k = 12*sisi
    return k

#-----------------------------------------------------------------------------

#tabung 
def volume_tabung(jari,tinggi): 
    V = 22/7 * jari**2 * tinggi
    return V 
def luas_tabung(jari,tinggi):
    L = 2 * 22/7 * jari * (jari + tinggi) 
    return L
def luas_selimut(jari,tinggi):
    S = 2*22/7*jari*tinggi
    return S 
def luas_alas_tabung(jari):
    A = 22/7*jari**2
    return A
#------------------------------------------------------------------------------

def luas_bola(r):
    L = 4 * 22/7 * r**2 
    return L
def volume_bola(r): 
    V = (4/3) * 22/7 * r**3 
    return V 
#------------------------------------------------------------------------------
def volume_kerucut(r,t) : 
    V = 1/3 * 22/7 * r**2 * t 
    return V 
def luas_kerucut(r,s) : 
    L = 22/7 * r *(r+s) 
    return L 
def alas_kerucut(r): 
    Ls= 22/7 * r**2 
    return Ls
def selimut_kerucut(r,s) : 
    LA = 22/7 * r * s 
    return LA
 




#Hasil akhir
def hasil_akhir_(pesan,nilai):
    print(f"{'-'*40:^40}\n")
    print(f"hasil dari perhitungan {pesan}  = {nilai:.2f}")


while True : 
    header()
    daftar()
    user_input = int(input("pilih opsi yang anda inginkan = "))
    if user_input == 1 : 
        header_balok()
        PANJANG,LEBAR,TINGGI = input_pertama_balok()
        print("""
1. Volume Balok 
2. Luas Permukaan Balok
3. Keliling Balok 
4. Diagonal Balok
""")
        user_balok = int(input("pilih no opsi yang anda inginkan = "))
        if user_balok == 1 : 
            VOLUME = volume(PANJANG,LEBAR,TINGGI)
            hasil_akhir_("Volume Balok",VOLUME)
        elif user_balok == 2 : 
            LUAS = luas_permukaan(PANJANG,LEBAR,TINGGI)
            hasil_akhir_("Luas Permukaan balok",LUAS)
        elif user_balok == 3 : 
            KELILING = keliling(PANJANG,LEBAR,TINGGI)
            hasil_akhir_("Keliling balok",KELILING)
        elif user_balok == 4 : 
            DIAGONAL = diagonal_ruang(PANJANG,LEBAR,TINGGI)
            hasil_akhir_("Diagonal balok",DIAGONAL)
    elif user_input == 2 : 
        header_KUBUS()
        user_kubus = float(input("masukan panjang sisi kubus anda = "))
        print("""
1. Volume Kubus
2. Luas Permukaan Kubus
3. Keliling kubus
""")
        user_kubus_dua = int(input("masukan opsi yang anda inginkan = "))
        if user_kubus_dua == 1 : 
            VOLUME_KUBUS = volume_kubus(user_kubus)
            hasil_akhir_("Volume Kubus",VOLUME_KUBUS)
        elif user_kubus_dua == 2 : 
            LUAS_kubus = luas_kubus(user_kubus)
            hasil_akhir_("Luas Permukaan Kubus",LUAS_kubus)
        elif user_kubus_dua == 3 :
            KELILING_KUBUS = keliling_kubus(user_kubus)
            hasil_akhir_("Keliling Kubus",KELILING_KUBUS)
        else : 
            continue

            

    elif user_input == 3 : 
        header_TABUNG()
        user_tabung1 = float(input("Masukan jari jari tabung  = "))
        user_tabung2 = float(input("Masukan tinggi tabung     = "))
        print("""
1. Volume Tabung
2. Luas Permukaan Tabung
3. Luas Selimut 
4. Luas Alas
""")
        user_tabung3 = int(input("masukan opsi yang anda inginkan = "))
        if user_tabung3 == 1 :
            VOLUME_TABUNG = volume_tabung(user_tabung1,user_tabung2)
            hasil_akhir_("Volume Tabung",VOLUME_TABUNG)
        elif user_tabung3 == 2 : 
            LUAS_TABUNG = luas_tabung(user_tabung1,user_tabung2)
            hasil_akhir_("Luas Permukaan Tabung",LUAS_TABUNG)
        elif user_tabung3 == 3 : 
            SELIMUT = luas_selimut(user_tabung1,user_tabung2)
            hasil_akhir_("Luas Selimut",SELIMUT)
        elif user_tabung3 == 4 : 
            ALAS = luas_alas_tabung(user_tabung1)
            hasil_akhir_("Luas Alas",ALAS)
        else : 
            continue
        

    elif user_input == 4 : 
        header_BOLA()
        input_user_bola = float(input("masukan jari jari bola = "))
        print("""
1. Volume Bola
2. Luas Permukaan Bola
""")
        input_user_bola2 = int(input("masukan opsi yang anda inginkan = "))
        if input_user_bola2 == 1 : 
            VOLUME_BOLA = volume_bola(input_user_bola)
            hasil_akhir_("Volume Bola",VOLUME_BOLA)
        elif input_user_bola2 == 2 : 
            LUAS_BOLA = luas_bola(input_user_bola)
            hasil_akhir_("Luas Permukaan Bola ",LUAS_BOLA)
        else : 
            continue
    elif user_input == 5 : 
        header_Kerucut()
        input_kerucut1 = float(input("masukan jari jari kerucut     = "))
        print("""
1. Volume kerucut
2. Luas Permukaan Kerucut
3. Luas Selimut Kerucut
4. Luas Alas kerucut
""")
        input4 = int(input("masukan opsi yang anda inginkan = "))
        if input4 == 1 : 
            T_kerucut = float(input("masukan tinggi kerucut        = "))
            VOLUME_KERUCUT = volume_kerucut(input_kerucut1,T_kerucut)
            hasil_akhir_("Volume Kerucut",VOLUME_KERUCUT)
        elif input4 == 2 : 
            G_pelukis = float(input("masukan panjang garis pelukis = "))
            LUAS_KERUCUT = luas_kerucut(input_kerucut1,G_pelukis)
            hasil_akhir_("Luas Permukaan Kerucut",LUAS_KERUCUT)
        
        elif input4 == 3 : 
            ALAS_KERUCUT = alas_kerucut(input_kerucut1)
            hasil_akhir_("Luas Alas Kerucut",ALAS_KERUCUT)
        elif input4 == 4 : 
            G_pelukis = float(input("masukan panjang garis pelukis = "))
            SELIMUT_KERUCUT = selimut_kerucut(input_kerucut1,G_pelukis)
            hasil_akhir_("Luas Selimut Kerucut",SELIMUT_KERUCUT)
        else : 
            continue 
    else : 
        continue 

    user_akhir = input("masi mau lanjut (y/n) = ")
    if user_akhir == "n" : 
        break
print(f'{"SELESAI:^40"}')
print(f"{'-'*40:^40}\n")


























