u_name = ["whatthefuck"]
pd = [12345678]

db={}
def main():
    print("-"*106)
    print("\t\t\t\t\tEMPLOYEE MANAGEMENT")  
    print("-"*106)
    print("""
            \t\t\t\t1) Add Employee 
            \t\t\t\t2) Display Details
            \t\t\t\t3) Update Information
            \t\t\t\t4) Delete Information
            \t\t\t\t5) Filtre/search 
          """)
    print("-"*106)
    
def add():
    while True:
        id = int(input("Enter your id : "))
    
        if id not in db:
            name = input("Enter your name : ")
            age =  int(input("Enter your age : "))
            department = input("Enter your Department : ")
            salary = int(input("Enter your salary : "))
            detail = {}
            detail["name"]=name
            detail["age"]=age
            detail["department"]=department
            detail["salary"]=salary
            db[id]=detail
            print("""
                
                \t\t\t\t< ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ >
                \t\t\t\t< .....Added successefully..... >
                \t\t\t\t< ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ >

                """)
            break
        else:
            print("\t\t\t\t .....ID is already exist ..... ")
            continue


def display():
    print("-"*106)
    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","NAME","AGE","DEPARTMENT","SALARY"))
    print("-"*106)
    for i in db:
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["age"],db[i]["department"],db[i]["salary"]))
        print("-"*106)

def update():
    while True:
        id =  int(input("Enter your id : "))
        if id in db:
            while True:
                print("""
                        UPDATE INFORMATION
                    1) UPDATE NAME
                    2) NUPDATE AGE
                    3) UPDATE DEPARTMENT
                    4) UPDATE SALARY
                    """)
                CH = int(input("Select your choice : "))
                if CH == 1:
                    n = input("Update your name : ")
                    db[id]["name"] = n
                    print("Name successfully updated!")
                    break
                elif CH == 2:
                    a = input("Update your age : ")
                    db[id]["age"] = a
                    print("Age successfully updated!")
                    break
                elif CH == 3:
                    d = input("Update your Department : ")
                    db[id]["department"] = d
                    print("Department Successfully updated!")
                    break
                elif CH == 4:
                    s = input("Update your salary : ")
                    db[id]["name"] = s
                    print("salary Successfully updated!")
                    break
                else:
                    print("Invalid Input.....")
                    continue
            break
        else:
            print("\t\t\t\t .....ID Does NOT exist! ..... ")
            continue

def delete():
    while True:
        id =  int(input("Enter your id : "))
        if id in db:
            del db[id]
            print("Successfully deleted!")
            break
        else:
            print("\t\t\t\t .....ID Does NOT exist! ..... ")
            continue

def filter():
    print("""
            1) Name
            2) Age
            3) Department
            4) Salary
        """)
    while True:
        c = int(input("Enter Your Choice : "))
        if c == 1:
            naav = input("Emter Your Name : ")
            for i in db:
                if naav == db[i]["name"]:
                    print("-"*106)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","NAME","AGE","DEPARTMENT","SALARY"))
                    print("-"*106)
                    for i in db:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["age"],db[i]["department"],db[i]["salary"]))
                        print("-"*106)
                else :
                    print("Not Present in Database")
            break              

        elif c == 2:
            vay = input("Enter Your age : ")
            for i in db:
                if vay == db[i]["age"]:
                    print("-"*106)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","NAME","AGE","DEPARTMENT","SALARY"))
                    print("-"*106)
                    for i in db:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["age"],db[i]["department"],db[i]["salary"]))
                        print("-"*106)
                else :
                    print("Not Present in Database")
            break  

        elif c == 3:
            dep = input("Enter Your department : ")
            for i in db:
                if dep == db[i]["department"]:
                    print("-"*106)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","NAME","AGE","DEPARTMENT","SALARY"))
                    print("-"*106)
                    for i in db:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["age"],db[i]["department"],db[i]["salary"]))
                        print("-"*106)
                else :
                    print("Not Present in Database")
            break    

        elif c == 4:
            sal = int(input("Enter salary: "))
            for i in db:
                if sal == db[i]["salary"]:
                    print("-"*106)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","NAME","AGE","DEPARTMENT","SALARY"))
                    print("-"*106)
                    for i in db:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["age"],db[i]["department"],db[i]["salary"]))
                        print("-"*106)
                else :
                    print("Not Present in Database")
            break            
                

        else:
            print("Invalid Input.....")
            continue

while True:
    for i in range(4,0,-1):
        print("\t\t\t\t< ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ >")
        username = input("\t\t\t\t\tEnter Username : ")
        password = int(input("\t\t\t\t\tEnter Password : "))
        print("\t\t\t\t< ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ >")

        if username == u_name[0] and password == pd[0]: 
            while True:
                main()
                Choice = int(input("What do you wanna do : "))
                if Choice == 1:
                    add()
                elif Choice == 2:
                    display()
                elif Choice == 3:
                    update()
                elif Choice == 4:
                    delete()
                elif Choice == 5:
                    filter()
                else :
                    print("\n\n\t\t\t\t\tXXXXX Invalid Input XXXXX\n\n")
                    continue
                c = input("Do you want to continue (y/n): ").lower()
                if c == "n":
                    break

        else:
            print(f"""
                  
\t\t\t\t\tXXXXX INVILD USERNAME OR PASSWORD XXXXX
\t\t\t\t\t\tXXXXX TRY AGAIN XXXXX
\t\t\t\t\tXXXXX YOU HAVE LEFT WITH {i-1} ATTEMPT XXXXX
                  
                  """)
    break
