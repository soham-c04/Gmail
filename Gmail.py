# Making Gmail using File Handler

import time
import os
from pickle import *

gm=open('Gmail.dat','ab+')
gm.close()
print('Loading Gmail')
t=3
while t>0:
    m,s=divmod(t,60)
    timer='{:02d}:{:02d}'.format(m,s)
    print('...',end=' ')
    time.sleep(1)
    t-=1
print('\n')
print('Gmail')
p=0
while p!='3':
    p=input('''Choose one of the options:-
    1. Create a new Gmail account.
    2. Sign in to your account.
    3. Exit
    Enter 1 or 2 or 3 to choose
    Enter #b to back\n''')
    if p=='1':
        Username=[]
        Gm=open('Gmail.dat','rb')
        try:
            while True:
                t=load(Gm)
                Username.append(t['Username'])
        except (KeyError,EOFError):
            Gm.close()
        fname=input("Enter your first name: ")
        if fname!='#b':
            lname=input("Enter your last name: ")
            while True:
                un=input("Enter your username: ")
                if '@gmail.com' not in un:
                    un=un+'@gmail.com'
                    
                if un in Username:
                    print('Username already taken')
                else:
                    break
            n=0
            while n!=1:
                pw=input('Enter your password: ')
                if len(pw)>=8:
                    n+=1
                else:
                    print('Your password should contain at least 8 characters')
            con=""
            while pw!=con:
                con=input('Confirm your password: ')
                if pw!=con:
                    print("Those passwords didn't match. Try again")
            DOB=input("Enter your Date of birth: ")
            phone=input("Enter your phone number: ")
            gen1=input("Enter your gender(m/f): ")
            if gen1=='m':
                gen='male'
            elif gen1=='f':
                gen='female'
            else:
                gen=gen1
            print("Account Created!")
            GM=open('Gmail.dat','ab')
            Ac={}
            Ac['Sl.No']=len(Username)+1
            Ac['Name']=fname.title()+' '+lname.title()
            Ac['Username']=un
            Ac['Password']=pw
            Ac['DOB']=DOB
            Ac['Phone number']=phone
            Ac['Gender']=gen
            Ac['Inbox']=[]
            Ac['Sent']=[]
            Ac['Draft']=[]
            dump(Ac,GM)
            GM.close()
        else:
            print()
    elif p=='2':
        Username=[]
        Gm=open('Gmail.dat','rb')
        try:
            while True:
                t=load(Gm)
                Username.append(t['Username'])
        except (KeyError,EOFError):
            Gm.close()
        if len(Username)==0:
            print('Create an gmail account first to get started')
        else:
            print('Avaiable Gmails are:')
            Gma=open('Gmail.dat','rb')
            try:
                while True:
                    t2=load(Gma)
                    print(t2['Sl.No'],end='. ')
                    print(t2['Username'])
            except EOFError:
                Gma.close()
            Sl_No=[]
            Name=[]
            Username=[]
            Password=[]
            DOB=[]
            Phone=[]
            Gender=[]
            f=0
            Gm=open('Gmail.dat','rb')
            try:
                while True:
                    t3=load(Gm)
                    Sl_No.append(t3['Sl.No'])
                    Name.append(t3['Name'])
                    Username.append(t3['Username'])
                    Password.append(t3['Password'])
                    DOB.append(t3['DOB'])
                    Phone.append(t3['Phone number'])
                    Gender.append(t3['Gender'])
            except EOFError:
                Gm.close()
            h1=1
            while h1==1:
                z2=input('Select the Gmail you want to sign in.(Enter 1,2... to choose) \n')
                if z2!='#b':
                    try:
                        z2=int(z2)
                        b=z2-1
                        if z2 in Sl_No:
                            print("HI! ",Name[b])
                            while True:
                                pw=input('Enter your password: ')
                                if pw=='#b':
                                    n=2
                                    break
                                elif pw==Password[b]:
                                    n=1
                                    h1=0
                                    break
                                else:
                                    print('Wrong password!')
                                    print("Enter your password again")
                        else:
                            print('Enter a valid number')
                    except:
                        print('Enter an integer')
                else:
                    n=0
                    break
            if n==1:
                print('Welcome, ',Name[b].split(' ')[0])
                a=0
                while a!=6:
                    gm=open("Gmail.dat",'rb')
                    try:
                        while True:
                            l=load(gm)
                            if l['Username']==Username[b]:
                                Draft=l['Draft']
                                Sent=l['Sent']
                                Inbox=l['Inbox']
                            
                    except EOFError:
                        gm.close()
                    a=0
                    try:
                        a=int(input('''Choose from one of the following options:
    1. Account Details
    2. Compose Email
    3. Inbox
    4. Sent
    5. Drafts
    6. Logout \n'''))
                    except:
                        print('Enter an integer')
                    if a==1:
                        a1=0
                        while a1!='#b':
                            Gm=open('Gmail.dat','rb')
                            Sl_No=[]
                            Name=[]
                            Username=[]
                            Password=[]
                            DOB=[]
                            Phone=[]
                            Gender=[]
                            try:
                                while True:
                                    t4=load(Gm)
                                    Sl_No.append(t4['Sl.No'])
                                    Name.append(t4['Name'])
                                    Username.append(t4['Username'])
                                    Password.append(t4['Password'])
                                    DOB.append(t4['DOB'])
                                    Phone.append(t4['Phone number'])
                                    Gender.append(t4['Gender'])
                            except EOFError:
                                Gm.close()
                            print('  1.Name: ',Name[b])
                            print('  2.Username: ',Username[b])
                            print('  3.Date of Birth: ',DOB[b])
                            print('  4.Phone Number: ',Phone[b])
                            print('  5.Gender: ',Gender[b])
                            print('  6.Change Password')
                            print('  7.Delete Account')
                            a1=input('Select any one to change \n')
                            l1={}
                            l2={}
                            l3={}
                            l4={}
                            l5={}
                            l6={}
                            if a1=='1':
                                name=input('Enter new name: ')
                                name1=name.title()
                                if name!='#b':
                                    print('Name updated succesfully')
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    l={}
                                    try:
                                        while True:
                                            l=load(gm1)
                                            if l['Username']==Username[b]:
                                                l['Name']=name1
                                            dump(l,gm)
                                    except EOFError:
                                        gm1.close()
                                        gm.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                            elif a1=='2':
                                print("\nUsername can't be changed \n")
                            elif a1=='3':
                                dob=input('Enter new Date of Birth: ')
                                if dob!='#b':
                                    print('Date of Birth updated succesfully')
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    l={}
                                    try:
                                        while True:
                                            l=load(gm1)
                                            if l['Username']==Username[b]:
                                                l['DOB']=dob
                                            dump(l,gm)
                                    except EOFError:
                                        gm1.close()
                                        gm.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                            elif a1=='4':
                                mobile=input('Enter new Phone Number: ')
                                if mobile!='#b':
                                    print('Phone Number updated succesfully')
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    l={}
                                    try:
                                        while True:
                                            l=load(gm1)
                                            if l['Username']==Username[b]:
                                                l['Phone number']=mobile
                                            dump(l,gm)
                                    except EOFError:
                                        gm1.close()
                                        gm.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                            elif a1=='5':
                                gen1=input('Enter new Gender: ')
                                if gen1!='#b':
                                    if gen1=='m':
                                        gen='male'
                                    elif gen1=='f':
                                        gen='female'
                                    else:
                                        gen=gen1
                                    print('Gender updated succesfully')
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    l={}
                                    try:
                                        while True:
                                            l=load(gm1)
                                            if l['Username']==Username[b]:
                                                l['Gender']=gen
                                            dump(l,gm)
                                    except EOFError:
                                        gm1.close()
                                        gm.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                            elif a1=='6':
                                pw=0
                                while pw!=Password[b] and pw!='#b':
                                    pw=input('Enter previous password: ')
                                    if pw!='#b':
                                        if pw==Password[b]:
                                            z=0
                                            while z!=1:
                                                pw1=input('Enter new password: ')
                                                if len(pw1)>=8:
                                                    z+=1
                                                else:
                                                    print('Your password should contain at least 8 characters')
                                            pw2=0
                                            while pw1!=pw2:
                                                pw2=input('Confirm new password: ')
                                            print('Password changed succesfully')
                                            gm1=open('Gmail.dat','rb')
                                            gm=open('temp.dat','wb')
                                            l={}
                                            try:
                                                while True:
                                                    l=load(gm1)
                                                    if l['Username']==Username[b]:
                                                        l['Password']=pw1
                                                    dump(l,gm)
                                            except EOFError:
                                                gm1.close()
                                                gm.close()
                                            os.remove('Gmail.dat')
                                            os.rename('temp.dat','Gmail.dat')
                                        else:
                                            print('Wrong password \nEnter password again')
                            elif a1=='7':
                                a2=input('Are you sure, you want to permanently delete your account?(y/n)')
                                if a2=='y':
                                    a1='#b'
                                    a=6
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    l={}
                                    try:
                                        while True:
                                            l=load(gm1)
                                            if l['Sl.No']>Sl_No[b]:
                                                l['Sl.No']=l['Sl.No']-1
                                            if l['Username']!=Username[b]:
                                                dump(l,gm)
                                    except EOFError:
                                        gm1.close()
                                        gm.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                            else:
                                y=0
                    elif a==2:
                        print('To:')
                        for i in range(len(Username)):
                            print(str(Sl_No[i])+'. '+Username[i])
                        while True:
                            pp1=input()
                            if pp1=='#b':
                                break
                            elif pp1=='':
                                print('You have to choose at least one gmail')
                            else:
                                try:
                                    p1=int(pp1)
                                    if p1==Sl_No[b]:
                                        print("Cannot send E-mail to yourself")
                                    elif p1 not in Sl_No:
                                        print('Enter a valid number')
                                    else:
                                        break
                                except:
                                    print('Enter an integer')
                        if pp1!='#b':
                            while True:
                                p2=input('Subject: ')
                                if p2=='':
                                    print('Subject cannot be empty')
                                else:
                                    break
                            l=[]
                            a=0
                            print('Multiline input is possible. Press enter 2 times to end writing')
                            while a!='':
                                a=input()
                                l.append(a)
                            g=0
                            while g!=1:
                                p3=input('Press 1 to send the mail and 2 to save as Draft. \n')
                                if p3=='1':
                                    print('E-mail sent.')
                                    g=1
                                    g=1
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    try:
                                        while True:
                                            t=load(gm1)
                                            if t['Username']==Username[b]:
                                                t['Sent'].append([len(t['Sent'])+1,Username[p1-1],p2,l])
                                            dump(t,gm)
                                    except EOFError:
                                        gm.close()
                                        gm1.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    try:
                                        while True:
                                            t=load(gm1)
                                            if t['Username']==Username[p1 -1]:
                                                t['Inbox'].append([len(t['Inbox'])+1,Username[b],p2,l,'u'])
                                            dump(t,gm)
                                    except EOFError:
                                        gm.close()
                                        gm1.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                                elif p3=='2':
                                    g=1
                                    gm1=open('Gmail.dat','rb')
                                    gm=open('temp.dat','wb')
                                    try:
                                        while True:
                                            t=load(gm1)
                                            if t['Username']==Username[b]:
                                                t['Draft'].append([len(t['Draft'])+1,Username[p1-1],p2,l])
                                            dump(t,gm)
                                    except EOFError:
                                        gm.close()
                                        gm1.close()
                                    os.remove('Gmail.dat')
                                    os.rename('temp.dat','Gmail.dat')
                                else:
                                    g=0
                    if a==3:
                        k=0
                        while k!=1:
                            print('INBOX')
                            print()
                            gm=open('Gmail.dat','rb')
                            try:
                                while True:
                                    l=load(gm)
                                    if l['Username']==Username[b]:
                                        Inbox=l['Inbox']
                            except EOFError:
                                gm.close()
                            print('0. Search(by subject)')
                            for i in range(len(Inbox)):
                                print(str(Inbox[i][0])+'. Subject-'+Inbox[i][2],end='')
                                if Inbox[i][4]=='u':
                                    print('----UNREAD')
                                else:
                                    print()
                                print('   From-'+Inbox[i][1])
                            jt=0
                            while jt!=1:
                                hh1=input('Choose one of the following E-mails: ')
                                print()
                                if hh1=='#b':
                                    k=1
                                    break
                                try:
                                    h1=int(hh1)
                                    if h1==0:
                                        q=input('Search-')
                                        q1=0
                                        for j in range(len(Inbox)):
                                            if q in Inbox[j][2]:
                                                print(str(Inbox[j][0])+'. Subject-',end='')
                                                q1+=1
                                                x=Inbox[j][2].split(q)
                                                i=1
                                                print(x[0],end='')
                                                try:
                                                    while True:
                                                        print('['+q+']'+x[i],end='')
                                                        i+=1
                                                except:
                                                    print(end='')
                                                if Inbox[j][4]=='u':
                                                    print('----UNREAD')
                                                else:
                                                    print() 
                                                print('   From-'+Inbox[j][1])
                                        if q1==0:
                                            print('No messages matched your search')
                                        print()
                                    elif 1<=h1<=len(Inbox):
                                        gm1=open('Gmail.dat','rb')
                                        gm=open('temp.dat','wb')
                                        try:
                                            while True:
                                                t=load(gm1)
                                                if t['Username']==Username[b]:
                                                    t['Inbox'][h1-1][4]='r'
                                                dump(t,gm)
                                        except EOFError:
                                            gm.close()
                                            gm1.close()
                                        os.remove('Gmail.dat')
                                        os.rename('temp.dat','Gmail.dat')
                                        print('Subject-'+Inbox[h1-1][2]+'\n'+'From-'+Inbox[h1-1][1])
                                        print()
                                        lt=[]
                                        for i in range(len(Inbox[h1-1][3])):
                                            print(Inbox[h1-1][3][i])
                                            lt.append(Inbox[h1-1][3][i])
                                        f1=input('Press 1 to  delete this E-mail,2 to forward and any other key to skip\n')
                                        if f1=='1':
                                            jt=1
                                            gm1=open('Gmail.dat','rb')
                                            gm=open('temp.dat','wb')
                                            l={}
                                            try:
                                                while True:
                                                    l=load(gm1)
                                                    if l['Username']==Username[b]:
                                                        for i in range(h1,len(Inbox)):
                                                            l['Inbox'][i][0]-=1
                                                        l['Inbox'].pop(h1-1)
                                                    dump(l,gm)
                                            except EOFError:
                                                gm1.close()
                                                gm.close()
                                            os.remove('Gmail.dat')
                                            os.rename('temp.dat','Gmail.dat')
                                        elif f1=='2':
                                            #####
                                            print('To:')
                                            for i in range(len(Username)):
                                                print(str(Sl_No[i])+'. '+Username[i])
                                            while True:
                                                pp1=input()
                                                if pp1=='#b':
                                                    break
                                                elif pp1=='':
                                                    print('You have to choose at least one gmail')
                                                else:
                                                    try: 
                                                        p1=int(pp1)
                                                        if p1==Sl_No[b]:
                                                            print("Cannot send E-mail to yourself")
                                                        elif p1 not in Sl_No:
                                                            print('Enter a valid number')
                                                        else:
                                                            jt=1
                                                            print('E-mail forwarded.')
                                                            gm1=open('Gmail.dat','rb')
                                                            gm=open('temp.dat','wb')
                                                            try:
                                                                while True:
                                                                    t=load(gm1)
                                                                    if t['Username']==Username[b]:
                                                                        t['Sent'].append([len(t['Sent'])+1,Username[p1-1],Inbox[h1-1][2],lt])
                                                                    dump(t,gm)
                                                            except EOFError:
                                                                gm.close()
                                                                gm1.close()
                                                            os.remove('Gmail.dat')
                                                            os.rename('temp.dat','Gmail.dat')
                                                            gm1=open('Gmail.dat','rb')
                                                            gm=open('temp.dat','wb')
                                                            try:
                                                                while True:
                                                                    t=load(gm1)
                                                                    if t['Username']==Username[p1-1]:
                                                                        t['Inbox'].append([len(t['Inbox'])+1,Username[b],Inbox[h1-1][2],lt,'u'])
                                                                    dump(t,gm)
                                                            except EOFError:
                                                                gm.close()
                                                                gm1.close()
                                                            os.remove('Gmail.dat')
                                                            os.rename('temp.dat','Gmail.dat')
                                                            break
                                                    except ValueError:
                                                      print('Enter an integer')
                                        else:
                                            jt=1    
                                    else:
                                        print('Enter a valid number')
                                except ValueError:
                                    print('Enter an integer')
                    if a==4:
                        k=0
                        while k!=1:
                            print('SENT')
                            print()
                            gm=open('Gmail.dat','rb')
                            try:
                                while True:
                                    l=load(gm)
                                    if l['Username']==Username[b]:
                                        Sent=l['Sent']
                            except EOFError:
                                gm.close()
                            print('0. Search(by subject)')
                            for i in range(len(Sent)):
                                print(str(Sent[i][0])+'. Subject-'+Sent[i][2]+'\n   '+'To-'+Sent[i][1])
                            jt=0
                            while jt!=1:
                                hh1=input('Choose one of the following E-mails: ')
                                print()
                                if hh1=='#b':
                                    k=1
                                    break
                                try:
                                    h1=int(hh1)
                                    if h1==0:
                                        q=input('Search-')
                                        q1=0
                                        for j in range(len(Sent)):
                                            if q in Sent[j][2]:
                                                print(str(Sent[j][0])+'. Subject-',end='')
                                                q1+=1
                                                x=Sent[j][2].split(q)
                                                i=1
                                                print(x[0],end='')
                                                try:
                                                    while True:
                                                        print('['+q+']'+x[i],end='')
                                                        i+=1
                                                except:
                                                    print()
                                                print('   To-'+Sent[j][1])
                                        if q1==0:
                                            print('No messages matched your search')
                                        print()
                                    elif 1<=h1<=len(Sent):
                                        print('Subject-'+Sent[h1-1][2]+'\n'+'To-'+Sent[h1-1][1])
                                        print()
                                        lt=[]
                                        for i in range(len(Sent[h1-1][3])):
                                            print(Sent[h1-1][3][i])
                                            lt.append(Sent[h1-1][3][i])
                                        f1=input('Press 1 to  delete this E-mail,2 to forward and any other key to skip\n')
                                        if f1=='1':
                                            jt=1
                                            gm1=open('Gmail.dat','rb')
                                            gm=open('temp.dat','wb')
                                            l={}
                                            try:
                                                while True:
                                                    l=load(gm1)
                                                    if l['Username']==Username[b]:
                                                        for i in range(h1,len(Inbox)):
                                                            l['Sent'][i][0]-=1
                                                        l['Sent'].pop(h1-1)
                                                    dump(l,gm)
                                            except EOFError:
                                                gm1.close()
                                                gm.close()
                                            os.remove('Gmail.dat')
                                            os.rename('temp.dat','Gmail.dat')
                                        elif f1=='2':
                                            print('To:')
                                            for i in range(len(Username)):
                                                print(str(Sl_No[i])+'. '+Username[i])
                                            while True:
                                                pp1=input()
                                                if pp1=='#b':
                                                    break
                                                elif pp1=='':
                                                    print('You have to choose at least one gmail')
                                                else:
                                                    try: 
                                                        p1=int(pp1)
                                                        if p1==Sl_No[b]:
                                                            print("Cannot send E-mail to yourself")
                                                        elif p1 not in Sl_No:
                                                            print('Enter a valid number')
                                                        else:
                                                            jt=1
                                                            print('E-mail forwarded.')
                                                            gm1=open('Gmail.dat','rb')
                                                            gm=open('temp.dat','wb')
                                                            try:
                                                                while True:
                                                                    t=load(gm1)
                                                                    if t['Username']==Username[b]:
                                                                        t['Sent'].append([len(t['Sent'])+1,Username[p1-1],Sent[h1-1][2],lt])
                                                                    dump(t,gm)
                                                            except EOFError:
                                                                gm.close()
                                                                gm1.close()
                                                            os.remove('Gmail.dat')
                                                            os.rename('temp.dat','Gmail.dat')
                                                            gm1=open('Gmail.dat','rb')
                                                            gm=open('temp.dat','wb')
                                                            try:
                                                                while True:
                                                                    t=load(gm1)
                                                                    if t['Username']==Username[p1-1]:
                                                                        t['Inbox'].append([len(t['Inbox'])+1,Username[b],Sent[h1-1][2],lt,'u'])
                                                                    dump(t,gm)
                                                            except EOFError:
                                                                gm.close()
                                                                gm1.close()
                                                            os.remove('Gmail.dat')
                                                            os.rename('temp.dat','Gmail.dat')
                                                            break
                                                    except ValueError:
                                                      print('Enter an integer')
                                        else:
                                            jt=1
                                    else:
                                        print('Enter a valid number')
                                except ValueError:
                                    print('Enter an integer')
                    if a==5:
                        k=0
                        while k!=1:
                            print('DRAFTS')
                            print()
                            gm=open('Gmail.dat','rb')
                            try:
                                while True:
                                    l=load(gm)
                                    if l['Username']==Username[b]:
                                        Draft=l['Draft']
                            except EOFError:
                                gm.close()
                            print('0. Search(by subject)')
                            for i in range(len(Draft)):
                                print(str(Draft[i][0])+'. Subject-'+Draft[i][2]+'\n   '+'To-'+Draft[i][1])
                            jt=0
                            while jt!=1:
                                hh1=input('Choose one of the following E-mails: ')
                                print()
                                if hh1=='#b':
                                    k=1
                                    break
                                try:
                                    h1=int(hh1)
                                    if h1==0:
                                        q=input('Search-')
                                        q1=0
                                        for j in range(len(Draft)):
                                            if q in Draft[j][2]:
                                                print(str(Draft[j][0])+'. Subject-',end='')
                                                q1+=1
                                                x=Draft[j][2].split(q)
                                                i=1
                                                print(x[0],end='')
                                                try:
                                                    while True:
                                                        print('['+q+']'+x[i],end='')
                                                        i+=1
                                                except:
                                                    print()
                                                print('   To-'+Draft[j][1])
                                        if q1==0:
                                            print('No messages matched your search')
                                        print()
                                    elif 1<=h1<=len(Draft):
                                        print('Subject-'+Draft[h1-1][2]+'\n'+'To-'+Draft[h1-1][1])
                                        print()
                                        lt=[]
                                        for i in range(len(Draft[h1-1][3])):
                                            print(Draft[h1-1][3][i])
                                            lt.append(Draft[h1-1][3][i])
                                        f1=input('Press 1 to  delete this E-mail,2 to forward,3 to continue writing and any other key to skip\n')
                                        if f1=='1':
                                            jt=1
                                            gm1=open('Gmail.dat','rb')
                                            gm=open('temp.dat','wb')
                                            l={}
                                            try:
                                                while True:
                                                    l=load(gm1)
                                                    if l['Username']==Username[b]:
                                                        for i in range(h1,len(Inbox)):
                                                            l['Draft'][i][0]-=1
                                                        l['Draft'].pop(h1-1)
                                                    dump(l,gm)
                                            except EOFError:
                                                gm1.close()
                                                gm.close()
                                            os.remove('Gmail.dat')
                                            os.rename('temp.dat','Gmail.dat')
                                        elif f1=='2':
                                            print('To:')
                                            for i in range(len(Username)):
                                                print(str(Sl_No[i])+'. '+Username[i])
                                            while True:
                                                pp1=input()
                                                if pp1=='#b':
                                                    break
                                                elif pp1=='':
                                                    print('You have to choose at least one gmail')
                                                else:
                                                    try: 
                                                        p1=int(pp1)
                                                        if p1==Sl_No[b]:
                                                            print("Cannot send E-mail to yourself")
                                                        elif p1 not in Sl_No:
                                                            print('Enter a valid number')
                                                        else:
                                                            jt=1
                                                            print('E-mail forwarded.')
                                                            gm1=open('Gmail.dat','rb')
                                                            gm=open('temp.dat','wb')
                                                            try:
                                                                while True:
                                                                    t=load(gm1)
                                                                    if t['Username']==Username[b]:
                                                                        t['Sent'].append([len(t['Sent'])+1,Username[p1-1],Draft[h1-1][2],lt])
                                                                    dump(t,gm)
                                                            except EOFError:
                                                                gm.close()
                                                                gm1.close()
                                                            os.remove('Gmail.dat')
                                                            os.rename('temp.dat','Gmail.dat')
                                                            gm1=open('Gmail.dat','rb')
                                                            gm=open('temp.dat','wb')
                                                            try:
                                                                while True:
                                                                    t=load(gm1)
                                                                    if t['Username']==Username[p1-1]:
                                                                        t['Inbox'].append([len(t['Inbox'])+1,Username[b],Draft[h1-1][2],lt,'u'])
                                                                    dump(t,gm)
                                                            except EOFError:
                                                                gm.close()
                                                                gm1.close()
                                                            os.remove('Gmail.dat')
                                                            os.rename('temp.dat','Gmail.dat')
                                                            break
                                                    except ValueError:
                                                      print('Enter an integer')
                                        elif f1=='3':
                                            print('Continue writing:-')
                                            jt=1
                                            y8=[]
                                            for i in range(len(Draft[h1-1][3])-1):
                                                print(Draft[h1-1][3][i])
                                                y8.append(Draft[h1-1][3][i])
                                            a=0
                                            while a!='':
                                                a=input()
                                                y8.append(a)
                                            gl=0
                                            while gl!=1:
                                                y9=input('Press 1 to send the mail and 2 to save as Draft. \n')
                                                if y9=='1':
                                                    print('E-mail sent.')
                                                    gl=1
                                                    gm1=open('Gmail.dat','rb')
                                                    gm=open('temp.dat','wb')
                                                    try:
                                                        while True:
                                                            t=load(gm1)
                                                            if t['Username']==Username[b]:
                                                                t['Sent'].append([len(t['Sent'])+1,Draft[h1-1][1],Draft[h1-1][2],y8])
                                                            dump(t,gm)
                                                    except EOFError:
                                                        gm.close()
                                                        gm1.close()
                                                    os.remove('Gmail.dat')
                                                    os.rename('temp.dat','Gmail.dat')
                                                    gm1=open('Gmail.dat','rb')
                                                    gm=open('temp.dat','wb')
                                                    try:
                                                        while True:
                                                            t=load(gm1)
                                                            if t['Username']==Draft[h1-1][1]:
                                                                t['Inbox'].append([len(t['Inbox'])+1,Username[b],Draft[h1-1][2],y8,'u'])
                                                            dump(t,gm)
                                                    except EOFError:
                                                        gm.close()
                                                        gm1.close()
                                                    os.remove('Gmail.dat')
                                                    os.rename('temp.dat','Gmail.dat')
                                                elif y9=='2':
                                                    gl=1
                                                    gm1=open('Gmail.dat','rb')
                                                    gm=open('temp.dat','wb')
                                                    try:
                                                        while True:
                                                            t=load(gm1)
                                                            if t['Username']==Username[b]:
                                                                t['Draft'].append([len(t['Draft']),Draft[h1-1][1],Draft[h1-1][2],y8])
                                                                t['Draft'].pop(h1-1)
                                                            dump(t,gm)
                                                    except EOFError:
                                                        gm.close()
                                                        gm1.close()
                                                    os.remove('Gmail.dat')
                                                    os.rename('temp.dat','Gmail.dat')
                                                else:
                                                    gl=0 
                                        else:
                                            jt=1   
                                    else:
                                        print('Enter a valid number')
                                except:
                                    print('Enter an integer')
    elif p=='3':
        print()
  
