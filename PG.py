import random
j=1 #this is a counter that enables the script to display a welcoming message.
#------------------------------------------------------------------------------------
def view():
    file = open('password_generator.txt','r+')
    read = file.read()
    if read != '':
        print(f"""-----------------------------------------------
Here are your passwords:

{read}

-----------------------------------------------""")
    else:
        print('No passwords were saved')
    file.close()
#------------------------------------------------------------------------------------
while True:
    if j==1:
        print("""
-----------------------------------------------
Welcome to the Password Generator!""")
    else :
        print("""-----------------------------------------------""")
    print("""\t G : Generate a new password.
\t N : Add a new password.
\t V : View saved passwords.
\t R : Repair the program.
\t E : Exit.
-----------------------------------------------""")
    a  = input('Your answer is:\n \t=>  ')
    answer = a.upper()
#------------------------------------------------------------------------------------
    if answer == 'G':
        password = ''

        while True:
            try:
                number_of_characters = int(input('N° of characters ?\n \t=>  '))
                break
            except ValueError :
                print('Please write an integer!')


        print("""Type of characters?
\t L : Letters and symbols.
\t N : Numbers.
\t R or [Any Key] : random.
-----------------------------------------------""")
        type_ch = input('\t=>  ')
        type_of_characters = type_ch.upper()

        if type_of_characters == 'L':
            a = 58
            b = 126
        elif type_of_characters == 'N':
            a = 48
            b = 57
        else:
            a = 33
            b = 126
        for i in range(number_of_characters):
            password = password +  chr(random.randint(a,b))
        print(f"Please copy your password:\n \t=>  {password} \n ")
        yes_or_no = input('Should I save your password ?\n \t=>  ')
        if yes_or_no.upper() == 'YES':
            account = input('To which account is this password assigned ?\n \t=>  ')
            file = open('password_generator.txt','r+')
            saved= file.read()
            if saved =='':
                file.write(account+': '+password)
            else:
                file.write('\n'+account+': '+password)
            file.close()
            view_my_passwords = input('Do you want to view your saved passwords ?\n \t=>  ')
            if view_my_passwords.upper() == 'YES':
                view()


    elif answer == 'V':
        view()
    elif answer == 'N':
        my_password = input("What's your password ?\n \t=>  ")
        account = input('To which account is this password assigned ?\n \t=>  ')
        file = open('password_generator.txt','r+')
        saved= file.read()
        if saved =='':
            file.write(account+': '+my_password)
        else:
            file.write('\n'+account+': '+my_password)
        file.close()
    elif answer =='R':
        print(' Warning!\n \tResetting the program will result in deleting saved passwords.')
        verification = input('Should you wish to continue ?\n \t=>  ')
        if verification.upper() == 'YES':
            file = open('password_generator.txt','w+')
            file.truncate(0)
            file.close()
            print('All saved passwords were deleted.')
        elif verification.upper() =='NO':
            print('No files were deleted.')
        else:
            print(" The program doesn't recognize your command.")
    elif answer =='E':
        print('Goodbye!')
        break
    else:
        print(" The program doesn't recognize your command.")

#----------------------------------------------------------------------------------------
    if answer !='E':
            Exit = ''
            message = 0

            while Exit !='E'and Exit!='C':
                if message!=0: #this message is only displayed if the user doesn't type correctly
                    print(" The program doesn't recognize your command.")
                e = input('Press E to Exit or C to continue.\n \t=>  ')
                Exit = e.upper()
                message = 1 #message changes but isn't displayed unless the Exit is different from 'E' or 'C'


            if Exit =='E':
                print('Goodbye!')
                break
            else:
                j=j+1
