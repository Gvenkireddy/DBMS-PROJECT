import os
import cx_Oracle
con = cx_Oracle.connect("shiva/open@localhost/xe")
cur = con.cursor()


# screen clear block
def cls():
    os.system("cls")


# already exists patient retrive block
def registered():
    p_id = int(input("\tEnter patient ID :"))
    cur.execute(f"select * from patient where pid={p_id}")
    print("\t                 .......PATIENT DETAILS.......")
    eid = int()
    print("\n  PID  EID   PNAME       PCELL_NO   PADDRESS")
    for i in cur:
        print(i)
        eid = int(i[1])
    # consult_doctor(p_id, eid)
    cur.execute(f"select * from doctor1 where eid = {eid}")
    print("\n\t                 .......DOCTOR DETAILS.......")
    print("  EID  DNAME    DQUALIFICATON")
    for i in cur:
        print(i)
    cls()

# new patient registration block
def new_patient():
    last = int()
    cur.execute("select count(pid) from patient")
    for i in cur:
        last = int(i[0])
    last = last + i
    print(last)
    pid = last
    pname = input("\tEnter Patient Name : ")
    pcell_no = int(input("\tEnter phone no : "))
    padress = input("\tEnter Address : ")
    eid = doctor1()
    cur.execute(f"insert into patient values({pid}, {eid}, '{pname}', {pcell_no}, '{padress}')")
    con.commit()
    print("Please Note your PatientID for future assistance ", pid)
    consult_doctor(last, eid)


# employee block
def doctor1():

    cur.execute("select * from doctor1")
    for i in cur:
        print("                       ", i)
    pic = int(input("select doctor : "))
    return pic


def consult_doctor(pid, eid):
    cls()
    print("\tConsulting Doctor")
    cur.execute(f"select * from doctor1 where eid = {eid}")
    print("\nDoctor Details")
    for i in cur:
        print(i)
    check = input("\nDoes Doctor wants to allocate Room : ").lower()
    if check == "yes":
        assign_room(pid, eid)


def assign_room(pid, eid):
    print("\nChecking Free Rooms")
    cur.execute("select rono,status from rooms where status ='NO'")
    for i in cur:
        print(i)
    pick = int(input("select Room no : "))
    cur.execute(f"update rooms set status='YES' , pid ={pid} , eid ={eid} where rono ={pick}")
    con.commit()
    print(f"\n{pick} is Now allocated to the Patient1{pid} by the Employee {eid} ")


def custom_query():
    p = True
    while p:
        print("\n\t1.Write Custom Query\n\t2.Display Custom Query\n\t3.Exit")
        n = int(input("Option : "))
        if n == 1:
            try:
                query = input("Write Your Custom Query : ")
                cur.execute(query)
                con.commit
            except:
                print("\n\tInvalid Systax  or not exit")

        elif n == 2:
            try:
                query = input("Display Your Custom Query : ")
                cur.execute(query)
                for i in cur:
                    print(i)
            except:
                print("\n\tInvalid Systax ")
        else:
            print("Exited Custom Query.....")
            p = False
            break



p = True
while p:
    print("\n\t1.Registered patient\n\t2.New Patient\n\t3.Custom Query\n\t4.Exit")
    opt = int(input("\nEnter Your option : "))
    if opt == 1:
        registered()
    elif opt == 2:
        new_patient()
    elif opt == 3:
        custom_query()
    else:
        print("Exited.........")
        p=False
        break





con.commit
cur.close()
con.close()
