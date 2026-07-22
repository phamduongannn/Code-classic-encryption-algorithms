#=============================================
class CTrithemius:
    def __init__(self, plaintext,ciphertext=""):
        self.plaintext=plaintext
        self.ciphertext=ciphertext
    #========================================
    def MaHoa(self):
        self.ciphertext=""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            if c!=' ':
                so = ord(c) - 65;
                so = (so+(i%26)) % 26
                self.ciphertext += chr(so+ 65)
            else:
                self.ciphertext += ' '
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            c=self.ciphertext[i]
            if c != ' ':
                so = ord(c)- 65
                so = (so - (i%26) + 26) % 26
                self.plaintext += chr(so+65)
            else:
                self.plaintext += ' '
        return self.plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    cTrithemius= CTrithemius(p)
    c = cTrithemius.MaHoa()
    print("Sau khi ma hoa= ", c)
    s= cTrithemius.GiaiMa()
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
