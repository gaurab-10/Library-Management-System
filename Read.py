dicti={}
borrowers={}
index=0


def read():
    """  This function read the file "Books.txt" and "borrowers.txt" and update the dicti and borrowers respectively.       """
    global index
    try:
        with open("Books.txt") as f:
            for line in f:
                (a,b,c,d,e)=line.split(",")
                dicti.update( {a:{"Book_Name":b,"Writer":c,"Quantity":d,"Price":e.strip("\n")}   }  )
        #print(dicti)
    except:
        print("Error occured while writing the file.")
    try:
        file=open("borrowers.txt","r") # reading the file borrowers.txt file.
        lines=file.readlines()
        for line in lines:
            index+=1
            (a,b,c,d,e,f,g,h,i)=line.split(",")
            a=int(a)
            b=b[6::]#name
            c=c[12::]#borrowerID
            d=d[6::]# book
            e=e[8::]# bookID
            f=f[10::] #price
            g=g[8::]# status
            h=h[10::]
            i=i[10::].strip("\n")
            borrowers.update({ a:{"Borrower_Name":b,"Book_Name":d,"BookID" :e,"id_":c,
                                      "Issued_Date":h,"price":f,"Return_Status":g,"Return_Date":i} })
        file.close()
        #print(borrowers)
    except:
           print("Error occured while reading the file")
