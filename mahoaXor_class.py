#========================================
class CXOR:  
    def MaHoa(self, p, key):
        ci=""
        for c in p:
            if c!=' ':
                so = ord(c) - 65;
                so = so ^ key
                ci += chr(so+ 65)
            else:
                ci += c
        return ci
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    key=3
    cXOR = CXOR()
    c= cXOR.MaHoa(p, key)
    print("Sau khi ma hoa= ", c)
    s= cXOR.MaHoa(c,key)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()


    
