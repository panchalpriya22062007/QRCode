#Email validation 
'''
email length >6
email must be alpha
in email only 1 @ 
space not allow
if have alpha must be lower
contains any digit
must have _,.,@

'''
email = input("Enter the Email: ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                for i in email:  
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue  
                    elif i == "_" or i == "." or i == "@":
                        continue  
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong email5")
                else:
                    print("Email is valid.")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")
