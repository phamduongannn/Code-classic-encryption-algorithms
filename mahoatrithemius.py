#========================================
def MaHoa(plaintext):
    ciphertext=""
    for i in range(len(plaintext)):
        c = plaintext[i]
        if c!=' ':
            so = ord(c) - 65;
            so = (so+(i%26)) % 26
            ciphertext = ciphertext+ chr(so+ 65)
        else:
            ciphertext=ciphertext+' '
    return ciphertext
#========================================
def GiaiMa(ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        c=ciphertext[i]
        if c != ' ':
            so = ord(c)- 65
            so = (so - (i%26) + 26) % 26
            plaintext = plaintext+ chr(so+65)
        else:
            plaintext = plaintext+' '
    return plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    c = MaHoa(p)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()


    
