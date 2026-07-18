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
            PGN = input("Name of PG: ")
            Type1 = input("Type of PG: ")
            Rent_Per_Month1 = float(input("Rent Per Month: "))
            Deposite1 = float(input("Deposite: "))
            Time1 = input("Timings: ")
            Food_Menu1 = input("Food Menu: ")
            Name1 = input("Name of Owner: ")
            Address1 = input("Address of PG: ")
            Area1 = input("Area:")
            Contact_No1 =input("For More Information Contact to This: ")
      
            details.append({"Category":"PG","Name":PGN,"Type":Type1,"Rent":Rent_Per_Month1,
                            "Deposite":Deposite1,"Time":Time1,"Food":Food_Menu1,"Owner":Name1,
                            "Address":Address1,"Area":Area1,"Contact":Contact_No1})    

        elif choice == "2":
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
            Area2 = input("Area:")
            Contact_No2=input("For More Information Contact to This: ")
            details.append({"Category":"Hostel","Name":HN,"Type":Type2,"Fees":Stay_Fees_Per_Month,"fees":Mess_Fees_Per_Month,
                            "Deposite":Deposite2,"Time":Time2,"Food":Food_Menu2,"Owner":Name2,"Warden":name2,
                            "Address":Address2,"Area":Area2,"Contact":Contact_No2})  
        elif choice == "3":
            RHFN = input("Name of House/Flat/Area/Apartment: ")
            Type3 = input("Type : ")
            Rent_Per_Month3 = float(input("Rent Per Month: "))
            Deposite3 = input("Deposite: ")
            Time3 = input("Timings: ")
            Name3 = input("Name of Owner: ")
            Address3 = input("Address : ")
            Area3 = input("Area:")
            Contact_No3 =input("For More Information Contact to This: ")
    
            details.append({"Category":"Rental House/Flat","Name":RHFN,"Type":Type3,"Rent":Rent_Per_Month3,
                            "Deposite":Deposite3,"Time":Time3,"Owner":Name3,
                            "Address":Address3,"Area":Area3,"Contact":Contact_No3})  
        

    elif choice == "2":
         if len(details) == 0:
             print("\n Welcome to gudsethu!")
             print("No Details Available!")
             continue
         
         print("\n Welcome to gudsethu!")
        
         print("1. PG")
         print("2. Hostel")
         print("3. Rental House/Flat")

         Category = input("Select Category: ")

         if Category == "1":
            selected = "PG"
         elif Category == "2":
              selected = "Hostel"
         elif Category == "3":
              selected = "Rental House/Flat"
         else:
             print("invalid Category!")
             continue
         Area = input("Enter Area: ")

         filtered = []

         for item in details:
            if item["Category"] == selected and item["Area"].lower() == Area.lower() :
               filtered.append(item)
         if filtered:
            print("\nAvailable:")
            for i, item in enumerate(filtered, 1):
                      
                print(f"{len(filtered)}. {item['Name']}")
            num = int(input("Select number: "))
            if 1 <= num <= len(filtered):
               item = filtered[num - 1]

               print("\n--- Details ---")
               for key, value in item.items():
                   print(f"{key}: {value}")
         else:
                print("Details are not Available in this Area!")  
    elif choice == "3":
        print("Thank You!")
        break
