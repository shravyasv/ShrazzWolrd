print("--- 💐 WELCOME TO gudsethu 🌉🛖 ---")
details = []

fields = {
    "PG": ["Name","Type", "Rent", "Deposit", "Timings", "Food", "Owner", "Address", "Area", "Contact"],
    "Hostel": ["Name","Type", "Stay Fees", "Mess Fees", "Deposit", "Timings", "Food", "Owner", "Warden", "Address", "Area", "Contact"],
    "Rental": ["Name","Type", "Rent", "Deposit", "Timings", "Owner", "Address", "Area", "Contact"],
    "Hotel": ["Name","Type", "Price", "Advance", "Address", "Area", "Contact"]
}

def add(category):
    d = {"Category": category}
    d.update({f: input(f"{f}: ") for f in fields[category]})
    details.append(d)

while True:
    choice = input("\n1.Member\n2.Visitor\n3.Exit\nChoice: ")

    if choice == "1":
        cat = input("Category (PG/Hostel/Rental/Hotel): ")
        if cat in fields:
            add(cat)
            print("Added ✅")
        else:
            print("Invalid category ❌")

    elif choice == "2":
        cat, area, type = input("Category(PG/Hostel/Rental/Hotel):"), input("Area: "),input("Type(Boy👦 / Girl👧): ")

        found = [x for x in details
                 if x.get("Category","").lower() == cat.lower()
                 and x.get("Area", "").lower() == area.lower()
                 and x.get("Type","").lower() == type.lower()]

        if found:
            for x in found:
                print("\nAvailable details🫠\n")
                print("\n".join(f"{k}: {v}" for k, v in x.items()
                                if k!="Category" and k!="Area" and k!="Type"))
        else:
            print("Details are not available 👎")

    elif choice == "3":
        print("Thank You 🙏|Have a Good Day 🫶")
        break
