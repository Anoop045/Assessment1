import re


def signup():
	f1 = open('userid.txt',"r")
	mail=input("Enter Email-ID:")
	pasw=input('Create a Password:')
	pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
	patterna='[a-z]'
	patternb='[A-Z]'
	patternc='\d'
	patternd='[@_!#$%^&*()<>?/|:}{~]'
	d=[]
	f=[]
	for i in f1:
		a,b=i.split(",")
		b=b.strip()
		d.append(a)
		f.append(b)
	di=dict(zip(d,f))
	if re.search(pattern, mail):
		if mail not in d:
			if len(pasw) not in range(6,16):
				print('password must contain minimum of 6 to maximum of 16 characters')
				signup()
			elif re.search(patterna,pasw) == None:
				print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
				signup()
			elif re.search(patternb,pasw) == None:
				print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
				signup()
			elif re.search(patternc,pasw) == None:
				print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
				signup()
			elif re.search(patternd,pasw) == None:
				print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
				signup()
			else:
				f1 = open('userid.txt',"a")
				f1.write(mail+','+pasw+ '\n')
				print('Registered successfully')
				home()
		else:
			print('User already exists.')
			login()

	else:
		print('Invalid Email-ID.')
		signup()


def login():
	f1=open('userid.txt','r')
	mail=input('Enter Registered Email-ID:')
	pasw=input('Enter your password:')
	if len(mail or pasw)>=1:
		d=[]
		f=[]
		for i in f1:
			a,b=i.split(",")
			b=b.strip()
			d.append(a)
			f.append(b)
		di=dict(zip(d,f))

		if mail in di:
			if pasw==di[mail]:
				print('Successfully Logged-In.')
			else:
				print('Password or Username is incorrect.')
				forgotpass()
		else:
			print('Username doesnot exist,please Register.')
			signup()



def forgotpass():
	f1=open('userid.txt','r')
	print("Password is incorrect,Do you want to register or retrieve password")
	option=input('Register again?(r)| Retrieve password (rp) | Change password(cp):')
	if option=='r':
		signup()
	elif option=='rp':
		print("Enter the Mail-ID used while registering.")
		mail=input("Email-ID: ")
		d=[]
		f=[]
		for i in f1:
			a,b=i.split(",")
			b=b.strip()
			d.append(a)
			f.append(b)
		di=dict(zip(d,f))
		if mail in d:
			p1=di[mail]
			print(p1)
		else:
			print('user not found,please register.')
	elif option=='cp':
		createpass()




def createpass():
	print("Enter Username to which new password should be created.")
	mail=input("Email-ID: ")
	f1=open('userid.txt','r')
	d=[]
	f=[]
	for i in f1:
		a,b=i.split(",")
		b=b.strip()
		d.append(a)
		f.append(b)
	di=dict(zip(d,f))
	if mail in d:
		pwdnew=input("Create a new password: ")
		if len(pwdnew) not in range(6,16):
			print('password must contain minimum of 6 to maximum of 16 characters')
			createpass()
		elif re.search('[a-z]',pwdnew) == None:
			print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
			createpass()
		elif re.search('[A-Z]',pwdnew) == None:
			print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
			createpass()
		elif re.search('\d',pwdnew) == None:
			print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
			createpass()
		elif re.search('[@_!#$%^&*()<>?/|:}{~]',pwdnew) == None:
			print('Password must contain minimum one special character,one digit,one uppercase and one lowercase character.')
			createpass()
		else:
			f1=open('userid.txt','a')
			di[mail]= pwdnew
			print('Password changed successfully.Please Login .')
			login()



def home(option = None):
	option = input('Register(r) | Login(l) :')
	if option=='r':
		signup()
	elif option=='l':
		login()
	else:
		print('Please choose one either option from above !')
		home()
home()








