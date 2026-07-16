details = []

while True:
    print("\n1.Member")
    print("2.visitor")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\n1.Paying Guest(pg)")
        print("2.Hostel")
        print("3.Rental House/Flat")
        choice = input("Enter choice: ")

        if choice == "1":
            Catogary1 = "PG"
            PGN = input("Name of PG: ")
            Type1 = input("Type of PG: ")
            Rent_Per_Month1 = float(input("Rent Per Month: "))
            Deposite1 = float(input("Deposite: "))
            Time1 = input("Timings: ")
            Food_Menu1 = input("Food Menu: ")
            Name1 = input("Name of Owner: ")
            Address1 = input("Address of PG: ")
            Contact_No1 =input("For More Information Contact to This: ")
      
            details.append([ Catogary1,PGN,Type1,Rent_Per_Month1,Deposite1,Time1,Food_Menu1,Name1,Address1,Contact_No1])    

        elif choice == "2":
            Catogary2 = "Hostel"
            HN = input("Name of Hostel: ")
            Type2 = input("Type of Hostel: ")
            Stay_Fees_Per_Month = float(input(" Stay Fees Per Month: "))
            Mess_Fees_Per_Month = float(input("Mess Fees Per Month: "))
            Deposite2 =input("Deposite: ")
            Time2 = input("Timings: ")
            Food_Menu2 = input("Food Menu: ")
            Name2 = input("Name of Owner: ")
            name2 = input("Name of Warden: ")
            Address2 = input("Address of Hostel: ")
            Contact_No2=input("For More Information Contact to This: ")
    
            details.append([ Catogary2,HN,Type2,Stay_Fees_Per_Month,Mess_Fees_Per_Month,Deposite2,Time2, Food_Menu2,Name2,name2,Address2,Contact_No2])    

        elif choice == "3":
            Catogary3 = "Rental House/Flat"
            RHFN = input("Name of House/Flat/Area/Apartment: ")
            Type3 = input("Type : ")
            Rent_Per_Month3 = float(input("Rent Per Month: "))
            Deposite3 = input("Deposite: ")1
            
            Time3 = input("Timings: ")
            Name3 = input("Name of Owner: ")
            Address3 = input("Address : ")
            Contact_No3 =input("For More Information Contact to This: ")
    
            details.append([ Catogary3,RHFN,Type3,Rent_Per_Month3,Deposite3,Time3,Name3,Address3,Contact_No3])
        

    elif choice == "2":

        for detail in details:
            if detail[0]=="PG":

               print("\nCatogary:",detail[0])
               print("Name:",detail[1])
               print("Type:",detail[2])
               print("Rent:",detail[3])
               print("Deposite:",detail[4])
               print("Time:",detail[5])
               print("Food Menu:",detail[6])
               print("Owner:",detail[7])
               print("Address:",detail[8])
               print("Contact:",detail[-1])

            elif detail[0]=="Hostel":

                 print("\nCatogary:",detail[0])
                 print("Name:",detail[1])
                 print("Type:",detail[2])
                 print("Stay Fees Per Month:",detail[3])
                 print("Mess Fees Per Month:",detail[34])
                 print("Deposite:",detail[5])
                 print("Time:",detail[6])
                 print("Food Menu:",detail[7])
                 print("Owner:",detail[8])
                 print("warden:",detail[9])
                 print("Address:",detail[10])
                 print("Contact:",detail[-1])

            elif detail[0]=="Rental House/Flat":

                 print("\nCatogary:",detail[0])
                 print("Name:",detail[1])
                 print("Type:",detail[2])
                 print("Rent:",detail[3])
                 print("Deposite:",detail[4])
                 print("Time:",detail[5])
                 print("Owner:",detail[6])
                 print("Address:",detail[7])
                 print("Contact:",detail[-1])
    elif choice == "3":
        print("Thank You")
        break
