import os
print("\n\n**************************************TESTER**************************************\n\n")
path="C:/Users/ADM/Desktop/Tester1/Tester/Source code"
while 1: 
    print("Enter the choice your intersted in:     1]Send \n\t\t\t\t\t2]Recive \n\t\t\t\t\t3]Append software and signed file \n\t\t\t\t\t4]Encryption of Software")
    choice=int(input("------------------->"))
    """Sender part choice"""
    if choice==1:
        print("******************************************************************************************************************")
        print("Send to 1]ECU \n\t2]PKI")
        choice_sender=int(input("------------------->"))
        if choice_sender==1:
            print("Select File which is to be sent ",end=" ")
            print("\n\t\t\t\t\t1]Send encrypted software which is appended with signature")  
            choice_sender_file=int(input("------------------->"))
            if choice_sender_file==1:                      
                for file in os.listdir(path):
                    if file.startswith("Send_finaldata_to_ECU"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break           
        if choice_sender==2:
            print("Select File which is to be sent ",end=" ")
            print("\n\t\t\t\t\t1]Request \n\t\t\t\t\t2]Encrypted Software \n\t\t\t\t\t")
            choice_sender_file=int(input("------------------->"))
            if choice_sender_file==1:
                for file in os.listdir(path):
                    if file.startswith("Send_ecu_public_key_rq"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break
            elif choice_sender_file==2:
                for file in os.listdir(path):
                    if file.startswith("Send_encryptedfile"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break   
    """Reciver Part Choice"""                                    
    if choice==2:
        print("******************************************************************************************************************")
        print("Recive from 1]ECU \n\t2]PKI") 
        choice_Reciver=int(input("------------------->"))
        if choice_Reciver==1:
            break
        elif choice_Reciver==2:
            print("Select File which is to be Recived ",end=" ")
            print("\n\t\t\t\t\t1]Signed File \n\t\t\t\t\t2]ECU Public Key \n\t\t\t\t\t")
            choice_Reciver_file=int(input("------------------->"))
            if choice_Reciver_file==1:
              for file in os.listdir(path):
                    if file.startswith("Recieve_Signed_file"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break                
            elif choice_Reciver_file==2:
                for file in os.listdir(path):
                    if file.startswith("Recieve_ECU_Public_key"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break                                                       
    elif(choice==3):
        print("******************************************************************************************************************")
        for file in os.listdir(path):
            if file.startswith("Append_software_signed"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())
                break
    elif(choice==4):
        print("******************************************************************************************************************")
        for file in os.listdir(path):
            if file.startswith("Encryption_software"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())                
    print("\n\n\n")        