import datetime

def fineCheck(isdDate, rtnDate):
    """ It takes two parameters isdDate and rtnDate and calculate the difference between those dates and find out the no of days.
        if result is >10 then, it subtracts the result with 10 and add 2 $ fine for each extra Days. If result<=10, it prints suitable message.
            """
    print("")
    year=int(isdDate[0:4:])
    month=int(isdDate[5:7:])
    date=int(isdDate[8::])
    isdDate=datetime.date(year,month,date)
    days=(rtnDate-isdDate).days
    if( days>10): # if user returns book after 10 days.
        extraDays=days-10
        totalFine=extraDays*2
        print("    >>>>>>>>>>>>>>>>>>>>>>>>>")
        print("")
        print("         Extra Days:",extraDays)
        print("")
        print("         TotalFine for",extraDays,"==",totalFine,"$")
        print("")
        print("        Book returned Sucessfully")
        print("")
        print("     >>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("")
    else:
            print("Book returned Sucessfully")
            print("")
