#========================================
def MaHoa(plaintext, key):
    ciphertext=""
    for c in plaintext:
        if c!=' ':
            so = ord(c) - 65;
            so = (so+key) % 26
            ciphertext = ciphertext+ chr(so+ 65)
        else:
            ciphertext=ciphertext+c
    return ciphertext
#========================================
def GiaiMa(ciphertext,key):
    plaintext = ""
    for c in ciphertext:
        if c != ' ':
            so = ord(c)- 65
            so = (so - key + 26) % 26
            plaintext = plaintext+ chr(so+65)
        else:
            plaintext = plaintext+c
    return plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    key=3
    c = MaHoa(p, key)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c,key)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
