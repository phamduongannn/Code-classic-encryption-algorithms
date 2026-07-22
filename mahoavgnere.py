#========================================
def MaHoa(plaintext, key):
    ciphertext=""
    for i in range(len(plaintext)):
        c = plaintext[i]
        vt_key=i% len(key)
        if c!=' ':
            so = ord(c) - 65;
            so_key=ord(key[vt_key])-65+1 #Tùy cách tính
            so = (so+so_key) % 26
            ciphertext = ciphertext+ chr(so+ 65)
        else:
            ciphertext=ciphertext+' '
    return ciphertext
#========================================
def GiaiMa(ciphertext,key):
    plaintext = ""
    for i in range(len(ciphertext)):
        c=ciphertext[i]
        vt_key=i%len(key)
        if c != ' ':
            so = ord(c)- 65
            so_key=ord(key[vt_key])-65+1 #?????
            so = (so - so_key + 26) % 26
            plaintext = plaintext+ chr(so+65)
        else:
            plaintext = plaintext+' '
    return plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    key="ABC"
    c = MaHoa(p, key)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c,key)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()



    
