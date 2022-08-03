import datetime

from Read import dicti
from Read import borrowers
from Read import index
from Read import read

from FineCheck import fineCheck

"""       This is the program of Library Management System which perform function of display book , borrow book and return book."""


def displayBooks():
        """ This function Iterate throught the dicti and if quantity of the book is greater than 0 then, it displays the book. """
        print("\n-----------List of Books----------")
        print("BooksID","\t","title")
        print("---------------------------------")
        for key,value in dicti.items():
            quantity=int(value["Quantity"])
            if(quantity>0):
                print(key,"\t\t",value.get("Book_Name"), " ______",value.get("Writer"))
        main()        
          

def borrowBooks():
    """ This function 1st takes bookID, userID and userName. If bookID and userID are already present in the borrowers.txt then, it prints error
message ,If not present and quantity of hte book is > than 0 then, it decrease the quantity of that book from dicti and update the "Books.txt"
         after that it updates the borrowers and "borrowers.txt". If quanitiy is ==0 then it prints suitalbe error message..        """
    count=0
    print("--------------")
    try:
        bookID=int(input("Enter the  Book ID:  ")) 
        if bookID==0:
                print("Invalid bookID")
                borrowBooks()
        bookID=str(bookID)        
    except:
        print("Please input valid Book ID..")
        borrowBooks()
    try:
        id_=int(input("Enter your id:  "))
        if id_==0:
                print("Invalid ID")
                borrowBooks()
        id_=str(id_)
    except:
        print("!!!!!     Please input valid ID..      ")
        borrowBooks()
    name=input("Enter your full name:  ")
    
    while(name==""):
        name=input("Enter your full name:  ")
        
    for key,value in borrowers.items():
        if value["BookID"] == bookID and value["id_"] == id_:
            print("------------------------")
            print("You cannot borrow same book twice")
            print("------------------------")
            count=1
            break
    if count==0:
        #--- Checking whether this bookID is present in librrary or not-
        if bookID in dicti.keys():
            numbers=int(dicti[bookID]["Quantity"])   # Accessing quantity value and converting it into integer.
            #---IF bookID is present and its quantity is greater than 0..--
            if numbers>0: # if no of book is greater than 0.
                global index
                index=index+1 
                book_Name=dicti[bookID]["Book_Name"]
                price=dicti[bookID]["Price"]
                numbers=numbers-1 
                dicti[bookID]["Quantity"]=str(numbers)
                #print(dicti[bookID]["Quantity"])
                try:
                    file=open("Books.txt","w")
                      # ---Writing the updated Quantity into file-
                    for key,value in dicti.items():
                        file.write("%s,%s,%s,%s,%s"% (key,value["Book_Name"],value["Writer"],value["Quantity"],value["Price"]) )
                        file.write("\n")
                    file.close()
                except:
                    print("File not found.")    
                issued_Date=datetime.datetime.now().strftime("%Y-%m-%d")
                print("---------------")
                borrowers.update({ index:{"Borrower_Name":name,"Book_Name":book_Name,"BookID" :bookID,"id_":id_,
                                      "Issued_Date":issued_Date,"price":price,"Return_Status":"Not returned","Return_Date":"null"} })
                #try:
                    # -Creating new file to store the information of borrowed books...
                file=open("borrowers.txt","w")
                total=0
                book=""
                list_=[]
                for key,value in borrowers.items():
                    if id_ in value["id_"]: # if userID is present in borrowers.
                        total=float(value["price"])+total # Calculating the total cost.
                        book=value["Book_Name"]
                        if not book in list_:
                                list_.append(book)
                    file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s"% (key,
                                                    " Name:"+value["Borrower_Name"],
                                                    " BorrowerID:"+value["id_"],
                                                    " Book:"+value["Book_Name"],
                                                    " BookID:"+value["BookID"],
                                                    " Price($):"+value["price"],
                                                    " Status:"+value["Return_Status"],
                                                    " ISD-Date:"+value["Issued_Date"],
                                                    " RTN_Date:"+value["Return_Date"]  ))
                    file.write("\n")
                file.close()
                #except:
                    #print("Error occured while writing the file...")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                print("    !!!!    Book issued Successfully !!!!")
                print("")
                print("               Borrowed Books::  ", list_)
                print("               Total cost:- ",total)
                print("")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # IF bookID is present and its quantity is 0..
            else:   
                print("----------------")
                print("Sorry ! Requested book is not available at the moment...")                 
        #-IF bookID is not present in dictionary keys        
        if not bookID in dicti.keys():
            print("----------------")
            print("Book ID not found..")       
    main()
        

def returnBook():
    """  It asks user for bookId and their id if both present in borrwers then, it increases the quantity and update file "books.txt". After that
it updates the borrowers with returnStatus true and with returnDate then it updates the ""borrowers.txt". It calls fineCheck function to check whether
 user returns book after 10 days or not.  """
    count=0
    print("--------------")
    try:
        bookID=int(input("Enter the  Book ID:  "))
        if bookID==0:
                print("Invalid bookID")
                returnBook()
        bookID=str(bookID)
    except:
        print("Please input valid Book ID..")
        returnBook()
    try:
        id_=int(input("Enter your id:  "))
        if id_==0:
                print("Invalid bookID")
                returnBook()
        id_=str(id_)
    except:
        print("!!!!!     Please input valid ID..      ")
        returnBook()
    for key, value in borrowers.items():
        if value["id_"]==id_ and value["BookID"]==bookID:   # If bookID and useriD present in borrowers.
            count+=1
            key_=key
            issued_Date=value["Issued_Date"]                # Accessing the date when the book was issued.
            quantity=int(dicti[bookID]["Quantity"])
            quantity+=1                                     # Increasing quantity of the book which has been returned.
            dicti[bookID]["Quantity"]=str(quantity)         # updating the dicti with updated value of quantity.
            
            try:
                ''' -------Updating the quantity in book file--------- '''
                file=open("Books.txt","w")
                for key,value in dicti.items(): # Updating Books.txt file from the updated dicti.
                    file.write("%s,%s,%s,%s,%s"%(key,value["Book_Name"],value["Writer"],value["Quantity"],value["Price"]))
                    file.write("\n")
                file.close()
            except:
                print("File not found...")
            # updating the  borrowers dictionary
            borrowers[key_]["Return_Status"]="Returned"
            return_Date=datetime.datetime.now().strftime("%Y-%m-%d")
            borrowers[key_]["Return_Date"]=return_Date
            
            try:
                file=open("borrowers.txt","w")    
                for key,value in borrowers.items():   # Updating borrowers.txt file from the updated dicti.
                    file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s"% (key,
                                                    " Name:"+value["Borrower_Name"],
                                                    " BorrowerID:"+value["id_"],
                                                    " Book:"+value["Book_Name"],
                                                    " BookID:"+value["BookID"],
                                                    " Price($):"+value["price"],
                                                    " Status:"+value["Return_Status"],
                                                    " ISD_Date:"+value["Issued_Date"],
                                                    " RTN_Date:"+value["Return_Date"] ) )

                    file.write("\n")
                file.close()
            except:
                print("Error occured while writing the file...")
            rtnDate=datetime.date.today() 
            fineCheck(issued_Date,rtnDate)     # Calling fineCheck method..
            main()
            
    # IF BookID and userID not matched in the dictionary....
    if count==0:
        print("!! No record found !!")
        main()                 

def main():
    response=input("  Enter: 'Q' to Quit,  'D' to Display available books,  'B' to borrow books,\n"+"'R' to return book:  ").lower()

    if response=="d":
        displayBooks()
        
    elif response=="b":
        borrowBooks()
        
    elif response=="r":
        returnBook()
        
    elif response=="q":
        print("Thanks for visiting the library.")
        
    else:
        print("Wrong input.")
        main()

read()
print("....Welcome to the Gaurab's Library..")
print("---------------------")
main()

    
