"""
Program for Payroll Management System.
"""
from pickle import dump, load
from os import remove, rename
   
class employee:
    def __init__(self, nempcode=0, nname="", nsector="",npost="", nsalary=0):
        """
        Constructor function

        Parameters
        ----------
        nempcode : Numeric, optional
            Employee Code. The default is 0.
        nname : String, optional
            Employee Name. The default is "".
        nsector : String, optional
            Sector in which employee works. The default is "".
        npost : String, optional
            Post of Employee. The default is "".
        nsalary : Numeric, optional
            Employee's salary. The default is 0.

        Returns
        -------
        None.

        """
        self.empcode=nempcode
        self.name=nname
        self.sector=nsector
        self.post=npost
        self.salary=nsalary
        
        
    def new_record(self):
        """
        To add new Employee record.

        Returns
        -------
        None.

        """
        self.empcode=int(input("Enter the Employee Number: "))
        self.name=input("Enter the name of the Employee: ")
        self.sector=input("Enter the sector Employee comes under: ")
        self.post=input("Enter the Designation/Grade of the Employee: ")
        self.salary=int(input("Enter the Basic Salary of the Employee: "))
    
        
    def display_records(self):
        """
        To display records.

        Returns
        -------
        None.

        """
        global s_no
        print("\t",
        "| {:>4d}. | {:>8d} | {:<25s} | {:<20s} | {:<15s} | {:>6d} | {:>8d} |".
        format(s_no, self.empcode, self.name, self.sector, self.post, 
               self.salary, int(self.salary*1.28+50)))
        
        print("\t","-"*109)
        s_no+=1
    
    
    def salary_slip(self, empcode):
        """
        To view salary slip of any employee.

        Parameters
        ----------
        empcode : Numeric
            Empoyee code whose salary slip is required.

        Returns
        -------
        None.

        """
        if self.empcode==empcode:
            date=input("Enter month & year(mm/yy): ")
            global count
            count+=1
            print("\n")
            print('\t',"{:^57s}".format("Company Name"))
            print('\t',"{:^57s}".format("Pay Slip : "+ months[int(date[:2])]+
                                        "-20"+str(date[3:])))
            
            print()
            print('\t',"Employee Name/Code:",self.name+"/"+ str(self.empcode))
            print('\t',"Designation/Grade:",self.post)
            print('\t',"-"*57)
            print('\t',"| {:^25s} | {:^25s} |".format("Earnings", 
                                                      "Deductions"))
 
            print('\t',"-"*57)
            print('\t',"| Basic:{:>19d} | PF:{:>22d} |".format(self.salary, 
                                                        int(self.salary*0.22)))
            
            print('\t',"| DA:{:>22d} | ESI:{:>21d} |".format(
                                                    int(self.salary*0.10), 0))
            
            print('\t',"| HRA:{:>21d} | Others:{:>18d} |".format(
                                                    int(self.salary*0.40), 50))
            
            print('\t',"-"*57)
            print('\t',"| {:^25s} | {:^25s} |".format("Total Earnings:  "+
                                                 str(self.salary*1.5),
                                                 "Total Deductions: "+
                                                 str(self.salary*0.22+50)))
            
            print('\t',"-"*57)
            print('\t',"| {:<53s} |".format("Net Payable Amount: Rs "+
                                       str(self.salary*1.28+50)))
            
            print('\t',"-"*57)

            
    def update_record(self):
        """
        To update any record.

        Returns
        -------
        None.

        """
        attribute=input("Enter key(A/B/C/D): ").upper()
        value=input("Enter new value: ")
        if attribute=="A":                  #A: to update name
            self.name=value
        elif attribute=="B":                #B: to update sector
            self.sector=value
        elif attribute=="C":                #C: to update post
            self.post=value
        elif attribute=="D":                #D: to update salary
            self.salary=int(value)



class overtime:
    def __init__(self, ndate="", nemps=[]):
        """
        Constructor function

        Parameters
        ----------
        ndate : String, optional
            Date of Overtime. The default is "".
        nemps : List, optional
            List of employee who worked overtime. The default is [].

        Returns
        -------
        None.

        """
        self.date=ndate
        self.emps=nemps

        
    def add_record(self):
        """
        To add new overtime record.

        Returns
        -------
        None.

        """
        self.emps=[]
        self.date=input("Enter date of overtime(dd/mm/yy): ")
        emps=input("Enter Employee codes(code1,code2,...): ")
        lst=emps.split(",")
        for emp in lst:
            
            file1=open('Files/payroll.dat',"rb")
            count=0
            try:                            #for referential integrity
                while True:
                    rec=load(file1)
                    if rec.empcode==int(emp):
                        count+=1
            except EOFError:
                file1.close()
                
            if count==1:
                if emp!='':
                    self.emps.append(emp.strip(" "))
            else:
                print("No record with Employee code "+ emp+
                      " stored in main datafile !")
                
        self.emps.sort()
        print("Record stored successfully.")

        
    def modify_record(self,date):
        """
        To modify overtime record.

        Parameters
        ----------
        date : String
            Date of which record is to be updated in (dd/mm/yy) format.

        Returns
        -------
        None.

        """
        if self.date==date:
            global count
            count+=1
            empid=input("Enter Employee Code to ADD/REMOVE it: ")
            for emp in self.emps:
                if emp==empid:
                    self.emps.remove(empid)
                    print("Entry of "+empid+" removed successfully.")
                    break
                
            else:                           #for referential integrity
                file1=open('Files/payroll.dat',"rb")
                try:
                    while True:
                        rec=load(file1)
                        if rec.empcode==int(empid):
                            count+=1
                except EOFError:
                    file1.close()
        
                if count==3:
                    self.emps.append(empid)
                    self.emps.sort()
                    print("Entry of "+empid+" added successfully.")
                else:
                    print("No record with Employee code "+empid+
                          " stored in main datafile !")

        
    def view_record(self,date):
        """
        To view stored data.

        Parameters
        ----------
        date : String
            Date of which records of overtime are required.

        Returns
        -------
        None.

        """
        if self.date==date:
            global count,s_no
            count+=1
            print("\n\n")
            print("\t {:^53s}".format("EMPLOYEES WHO WORKED OVERTIME ON "+
                                  months[int(date[3:5])].upper()+
                                  "-20"+date[6:]))
            
            print("\t", "-"*53)
            print("\t", '| {:^5s} | {:^13s} | {:^25s} |'.
                  format("S.No.", "Employee Code", "Employee Name"))
            
            print("\t", "-"*53)
            file1=open('Files/payroll.dat',"rb")
            try:
                while True:
                    rec=load(file1)
                    for emp in self.emps:
                        if int(emp)==rec.empcode:
                            print("\t", '| {:>4d}. | {:>13d} | {:<25s} |'.
                                  format(s_no, rec.empcode, rec.name))
                            
                            print("\t", "-"*53)
                            s_no+=1
            except EOFError:
                file1.close()
                
            if self.emps==[]:
                print("\t", "| {:^49s} |".format("No records stored"))
                print("\t", "-"*53)
                

class attendance:
    def __init__(self, nmonth='', nrecord=dict()):
        """
        Constructor function.

        Parameters
        ----------
        nmonth : String, optional
            Month of attendance in (mm/yy) format. The default is ''.
        nrecord : Dictionary, optional
            Key:Value pairs of Employee code and respective monthly attendance.
            The default is dict().

        Returns
        -------
        None.

        """
        self.month=nmonth
        self.record=nrecord
        
        
    def input_records(self):
        """
        To add new monthly attendance record.

        Returns
        -------
        None.

        """
        self.record={}
        self.month=input("Enter month(mm/yy): ")
        ans="y"
        while ans!="n":
            empcode=int(input("Enter Employee code: "))
            
            file1=open('Files/payroll.dat',"rb")
            count=0
            try:                            #for referential integrity
                while True:
                    rec=load(file1)
                    if rec.empcode==empcode:
                        count+=1
            except EOFError:
                file1.close()
                
            if count==1:
                attendance=int(input("Enter Empoyee's Attendance: "))
                self.record[empcode]=attendance
            else:
                print("No record with Employee code "+ str(empcode)+
                      " stored in main datafile !")
            
            ans=input("Add more records([y]/n): ")
            
            
    def modify_record(self, month):
        """
        To modify monthly attendance.

        Parameters
        ----------
        month : String
            Month of attendance in (mm/yy) format.

        Returns
        -------
        None.

        """
        if month==self.month:
            global count
            count+=1
            empid=input("Enter Employee Code to ADD/REMOVE it: ")
            
            if int(empid) in self.record:
                del self.record[int(empid)]
                print("Entry of "+empid+" removed successfully.")
                
            else:
                file1=open('Files/payroll.dat',"rb")
                try:                        #for referential integrity
                    while True:
                        rec=load(file1)
                        if rec.empcode==empid:
                            count+=1
                except EOFError:
                    file1.close()
                    
                if count==2:
                    attendance=int(input("Enter Employee's Attendance: "))
                    self.record[int(empid)]=attendance
                    print("Attendance of "+empid+" added successfully.")
                else:
                    print("No record with Employee code "+ str(empid)+
                          " stored in main datafile !")     
        
            
    def view_attendance(self, nmonth):
        """
        To view monthly attendance of any month.

        Parameters
        ----------
        nmonth : String
            Month whose records are required in (mm/yy) format.

        Returns
        -------
        None.

        """
        if self.month==nmonth:
            global count,s_no
            count+=1
            file1=open('Files/payroll.dat', "rb")
            print("\n")
            print("\t","{:^91s}".format("MONTHLY ATTENDANCE OF "+
                                   months[int(nmonth[:2])].upper()+"-20"+
                                   nmonth[3:]))
            
            print("\t","-"*91)
            print("\t","| {:^5s} | {:^8s} | {:^25s} | {:^19s} | {:^18s} |".
                  format("S.No.","EMP CODE","EMPLOYEE NAME",
                         "ACTUAL WORKING DAYS","TOTAL WORKING DAYS"))
            
            print("\t","-"*91)
            try:
                while True:
                    rec=load(file1)
                    for emp in self.record:
                        if emp==rec.empcode:
                            print("\t",
                        "| {:>4d}. | {:>8d} | {:<25s} | {:>19d} | {:>18d} |".
                        format(s_no, rec.empcode, rec.name, self.record[emp], 
                               26))
            
                            print("\t","-"*91)
                            s_no+=1
            except EOFError:
                file1.close()
                
            if self.record=={}:
                print("\t","| {:^87s} |".format("No records stored"))
                print("\t","-"*91)
                    

def create_datafile():
    """
    To create/reset Datafiles of Payroll Management.

    Returns
    -------
    None.

    """
    open("Files/payroll.dat","wb").close()
    open("Files/overtime.dat","wb").close()
    open("Files/Files/attendance.dat","wb").close()
                
            
#----------------------------------main---------------------------------------
menu='''
----------------------------------
| {:^30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
'''.format("MENU", 
            " 1. Create/Reset Datafiles.",    " 2. Add New Record.",
            " 3. View Records stored.",       " 4. Modify Records.",
            " 5. Delete Employee Records.",   " 6. View Salary Slip.",
            " 7. Add Overtime Record.",       " 8. Modify Overtime Record.", 
            " 9. View Overtime Records.",     "10. Add Monthly Attendance.",
            "11. Modify Monthly Attendance.", "12. View Monthy Attendance.")

attributes="""
A: To update name
B: To update sector
C: To update post
D: To update salary 
"""

rec=employee()
orec=overtime()
arec=attendance()
months={1:"Jan",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",
        8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

act='y'
while act!='n':
    print(menu)
    ans=input("Enter serial number of the task you want to perform: ")
   
    if ans=="1":
        create_datafile()
        print("Datafile created/reset successfully.")


    elif ans=="2":
        with open("Files/payroll.dat","ab") as file1:
            rec.new_record()
            dump(rec, file1)
            print("New record added successfully.")
            file1.flush()
            file1.close()

        
    elif ans=="3":
        print("\n\n\t{:^109s}".format("EMPLOYEES DETAILS"))
        print("\t","-"*109)
        print("\t",
        "| {:^5s} | {:^8s} | {:^25s} | {:^20s} | {:^15s} | {:^6s} | {:^8} |".
        format("S.No.","EMP CODE", "EMPLOYEE NAME", "SECTOR", "POST", "BASIC", 
               "NET PAY"))
        
        print("\t","-"*109)
        s_no=1
        with open('Files/payroll.dat',"rb") as file1:
            try:
                while True:
                    rec=load(file1)
                    rec.display_records()
            except EOFError:
                file1.close()


    elif ans=="4":
        empid=int(input("Enter Employee Code: "))
        with open("Files/payroll.dat","rb") as file1:
            with open("new.dat","wb") as nfile:
                try:
                    while True:
                        rec=load(file1)
                        if rec.empcode==empid:
                            print(attributes)
                            rec.update_record()
                            dump(rec, nfile)
                            nfile.flush()
                            print("Record updated successfully.")
                        else:
                            dump(rec, nfile)
                            nfile.flush()
                except EOFError:
                    nfile.close()
                    file1.close()
        remove("Files/payroll.dat")
        rename("new.dat", "Files/payroll.dat")


    elif ans=="5":
        empid=input("Enter Employee code: ")

#       to delete record from 'Files/payroll.dat'
        with open('Files/payroll.dat',"rb") as file1:
            with open('new.dat',"wb") as nfile:
                try:
                    while True:
                        rec=load(file1)
                        if int(empid)!=rec.empcode:
                            dump(rec, nfile)
                            nfile.flush()
                except EOFError:
                    file1.close()
                    nfile.close()
        remove("Files/payroll.dat")
        rename('new.dat', "Files/payroll.dat")
        
#       to delete record from 'Files/overtime.dat'
        with open('Files/overtime.dat',"rb") as file2:
            with open('new.dat',"wb") as nfile:
                try:
                    while True:
                        orec=load(file2)
                        if empid in orec.emps:
                            orec.emps.remove(empid)
                        dump(orec, nfile)
                        nfile.flush()
                except EOFError:
                    file2.close()
                    nfile.close()
        remove('Files/overtime.dat')
        rename('new.dat', 'Files/overtime.dat')
        
#       to delete record from 'Files/Files/attendance.dat'
        with open('Files/Files/attendance.dat',"rb") as file3:
            with open('new.dat',"wb") as nfile:
                try:
                    while True:
                        arec=load(file3)
                        if empid in arec.record:
                            del arec.record[empid]
                        dump(arec, nfile)
                except EOFError:
                    file3.close()
                    nfile.close()
        remove('Files/Files/attendance.dat')
        rename('new.dat', 'Files/Files/attendance.dat')
        
        print("Record with Employee Code "+empid+" is deleted successfully.")


    elif ans=="6":
        empcode=int(input("Enter Employee's Code: "))
        file1=open("Files/payroll.dat","rb")
        count=0
        try:
            while True:
                rec=load(file1)
                rec.salary_slip(empcode)
        except EOFError:
            file1.close()
            if count==0:
                print("No record with this code is stored.")
                            

    elif ans=="7":
        with open("Files/overtime.dat","ab") as file2:
            orec.add_record()
            dump(orec, file2)
            file2.close()

        
    elif ans=="8":
#       to display stored dates
        print("-"*16)
        print("| Dates Stored |")
        print("-"*16)
        with open('Files/overtime.dat',"rb") as file2:
            try:
                while True:
                    orec=load(file2)
                    print("| {:>12s} |".format(orec.date))
                    print("-"*16)
            except EOFError:
                file2.close()
                
#       to view and modify records
        ndate=input("Enter date(dd/mm/yy): ")
        count=0
        s_no=1
        with open('Files/overtime.dat',"rb") as file2:
            with open('new.dat',"wb") as nfile:
                try:
                    while True:
                        orec=load(file2)
                        orec.view_record(ndate)
                        orec.modify_record(ndate)
                        dump(orec, nfile)
                except EOFError:
                    file2.close()
                    nfile.close()
                if count==0:
                    print("No record available for date "+ndate+" to modify.")
                    
        remove('Files/overtime.dat')
        rename('new.dat', 'Files/overtime.dat')

        
    elif ans=="9":
#       to display stored dates
        print("-"*16)
        print("| Dates Stored |")
        print("-"*16)
        with open('Files/overtime.dat',"rb") as file2:
            try:
                while True:
                    orec=load(file2)
                    print("| {:>12s} |".format(orec.date))
                    print("-"*16)
            except EOFError:
                file2.close()
                
#       to view records
        ndate=input("Enter date(dd/mm/yy): ")
        count=0
        s_no=1
        with open('Files/overtime.dat',"rb") as file2:
            try:
                while True:
                    orec=load(file2)
                    orec.view_record(ndate)
            except EOFError:
                file2.close()
                if count==0:
                    print("No record available for date "+ndate+".")

                    
    elif ans=="10":
        with open('Files/Files/attendance.dat', "ab") as file3:
            arec.input_records()
            dump(arec, file3)
            file3.flush()
            file3.close()
            

    elif ans=="11":
#       to display stored months
        print("-"*17)
        print("| MONTHS STORED |")
        print("-"*17)
        for nmonth in months:
            with open('Files/Files/attendance.dat', "rb") as file3:
                try:
                    while True:
                        arec=load(file3)
                        if nmonth==int(arec.month[:2]):
                            print("| {:>13s} |".format(
                                months[int(arec.month[:2])]+
                                "-20"+ arec.month[3:]))
                    
                            print("-"*17)
                except:
                    file3.close()
        
#       to view and modify records 
        month=input("Enter Month(mm/yy): ")
        count=0
        s_no=1
        with open('Files/Files/attendance.dat',"rb") as file3:
            with open('new.dat', "wb") as nfile:
                try:
                    while True:
                        arec=load(file3)
                        arec.view_attendance(month)
                        arec.modify_record(month)
                        dump(arec, nfile)
                except EOFError:
                    file3.close()
                    nfile.close()
                    
        if count==0:
            print("No record of month "+months[int(month[:2])]+
                  "-20"+month[3:]+".")
    
        remove("Files/Files/attendance.dat")
        rename('new.dat', 'Files/Files/attendance.dat')
        
            
    elif ans=="12":
#       to display stored months
        print("-"*17)
        print("| MONTHS STORED |")
        print("-"*17)
        for nmonth in months:
            with open('Files/Files/attendance.dat', "rb") as file3:
                try:
                    while True:
                        arec=load(file3)
                        if nmonth==int(arec.month[:2]):
                            print("| {:>13s} |".format(
                                months[int(arec.month[:2])]+
                                "-20"+ arec.month[3:]))
                    
                            print("-"*17)
                except:
                    file3.close()
        
#       to view records
        s_no=1
        month=input("Enter Month(mm/yy): ")
        count=0
        with open('Files/Files/attendance.dat',"rb") as file3:
            try:
                while True:
                    arec=load(file3)
                    arec.view_attendance(month)
            except EOFError:
                file3.close()
                if count!=1:
                    print("No record of month "+months[int(month[:2])]+"-20"+
                          month[3:]+".")
                    
    else:
        print("Invalid input !!!")


    act=input("Do you want to perform more tasks([y]/n): ")

else:
    print("Thanks for using this program.")
    
    