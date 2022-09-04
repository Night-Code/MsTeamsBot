import re
from datetime import datetime as date
from datetime import datetime
def ctime():
    day=date.today().strftime("%A")
    time= datetime.now()
    current_time = time.strftime("%H:%M:%S")
    return current_time,day;

def print_table(file):
    file=open(file)
    handle=file.read()
    print("TIME TABLE:\n")
    for i in handle.splitlines():
        str=i.replace("="," ")
        str=str.replace("->"," ")
        str=str.replace(","," ")
        print(str+"\n")
    file.close()

def sort(file,str):
    rh=open(file,'w')
    ls=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    co=0
    l=len(str.strip("\n"))
    for j in ls:
        for i in str.split('\n'):
            lst=i.split('->')
            if lst[0].lower()==j.lower():
                co=co+1
                if(co==l):
                    rh.write(i)
                else:
                    rh.write(i+'\n')
    rh.close()

def str_file(file,str):
    if len(str)!=0:
        stri=str
    else:
        rh=open(file,'r')
        stri=rh.read()
        rh.close()
    wh=open(file,'w')
    count=0
    for i in stri.split('\n'):
        count=count+1
        if len(stri.split("\n"))==count:
            wh.write(i)
        else:
            wh.write(i+"\n")
    wh.close()

def create_file(file,str):
    w=open(file,'r+')
    print("""\nEnter the time table\nFormat\nDay~Start Time~Subject Name~End Time\nMonday~10:15~CSE-4 Python~11:45""")
    q=True
    stri=''
    lt=[]
    while(True):
        st=input("\nEntry:\n")
        st = st.split("~")
        if len(st)==4:
            lt.append(st[0]+'->'+st[1]+'='+st[2]+'='+st[3])
            w.write(st[0]+'->'+st[1]+'='+st[2]+'='+st[3]+'\n')
            stri=stri+st[0]+'->'+st[1]+'='+st[2]+'='+st[3]+'\n'
        else:
            print("\nWrong Format!\n")
        ans=input("\nFurther enteries?(Y/N)\n")
        if not (ans.lower()=='y'):
            break
    w.close()
    if len(str)!=0:
        for i in lt:
            if i.strip()=='':
                continue
            str=str+"\n"+i
        stri=str
        str_file(file,str)
    sort(file,stri)
    print_table(file)

def table_change():
    handle=input('Enter a name of the file:\n')
    rh=open(handle,'a')
    rh.close()
    rh=open(handle)
    str=rh.read()
    rh.close()
    if len(str)==0:
        create_file(handle,str)
    change=input("Want any change in the time table ?(Y/N)\n")
    if change.lower()=='y':
        while(change.lower()=='y'):
            co=0
            count=0
            rh=open(handle,'r')
            str=stri=rh.read()
            rh.close()
            print_table(handle)
            wh=open(handle,'w')
            day=input("Enter the day you want to make change in:\n")
            for i in str.split('\n'):
                if i.strip()=='':
                    continue
                count=count+1
                sp=i.split('->')
                if sp[0].lower()==day.lower():
                    c=0
                    co=co+1
                    cou=0
                    each=sp[1].strip().split(',')
                    st=input("Enter the start time\n").split(':')
                    sub=input("Enter the subject name\n")
                    lt=input("Enter the end time\n")
                    for j in each:
                        j=j.strip()
                        cou=cou+1
                        t_s=j.split('=')
                        time=t_s[0].split(':')
                        if int(time[0])==int(st[0]) and int(time[1])<=int(st[1]):
                            c=1
                            if cou==len(each):
                                i=i.replace(j,(st[0]+":"+st[1]+"="+sub+"="+lt))
                            else:
                                i=i.replace(j,(st[0]+":"+st[1]+"="+sub+"="+lt+","))
                    if c!=1:
                        i=i+", "+st[0]+":"+st[1]+"="+sub+"="+lt
                print("\n")
                if len(stri.split("\n"))==count:
                    wh.write(i)
                else:
                    wh.write(i+"\n")
            wh.close()
            if co==0:
                create_file(handle,str)
            change=input("Want any more change in the time table ?(Y/N)\n")
    else:
        stri=""
        str_file(handle,stri)
    return handle

def day_check():
    handle=table_change()
    fh=open(handle)
    current_time,day=ctime()
    f=0
    c_time=current_time.split(':')
    for i in fh:
        sp=i.split('->')
        if sp[0]==day:
            each=sp[1].strip().split(',')
            for j in each:
                t=j.strip().split('=')
                st=t[0].split(':')
                if int(st[0])==int(c_time[0].strip()) and  int(st[1])<=int(c_time[1]):
                    print("true")
                    f=1
                    print(t[1])
                    return 1,t[1],t[0];
                else:
                    continue
    if f==0:
        return 0,"Bot","12:00";
    fh.close()
    print_table(handle)
