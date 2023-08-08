import os
print("---------------------------PKI----------------------------------------")
path="D:/Academics/6TH SEM/bosch/communication/PKI/Source code"
while 1: 
    print("Enter the choice your intersted in:     1]Send \n\t\t\t\t\t2]Recive \n\t\t\t\t\t3]generate Keys \n\t\t\t\t\t4]Decrypt Software to sign \n\t\t\t\t\t5]sign the Software")
    choice=int(input("------------------->"))
    """Sender part choice"""
    if choice==1:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Send to 1]ECU \n\t2]Tester")
        choice_sender=int(input("------------------->"))
        if choice_sender==1:
            print("Send to 1]ECU Private key \n\t2]Tester public key")
            choice_sender_key1=int(input("------------------->"))  
            if choice_sender_key1==1:
                for file in os.listdir(path):
                    if file.startswith("Send_ECU_private_key"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break            
            elif choice_sender_key1==2:
                for file in os.listdir(path):
                    if file.startswith("Send_Tester_public_key"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break             
        if choice_sender==2:
            print("Select File which is to be sent ",end=" ")
            print("\n\t\t\t\t\t1]Public Key \n\t\t\t\t\t2]Signed File \n\t\t\t\t\t")
            choice_sender_file=int(input("------------------->"))
            if choice_sender_file==1:
                for file in os.listdir(path):
                    if file.startswith("Send_ECU_public_key"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break
            elif choice_sender_file==2:
                for file in os.listdir(path):
                    if file.startswith("Send_signed_file"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break   
    """Reciver Part Choice"""                                    
    if choice==2:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Recive from 1]ECU \n\t2]Tester") 
        choice_Reciver=int(input("------------------->"))
        if choice_Reciver==1:
            print("Select File which is to be Recived ",end=" ")
            print("\n\t\t\t\t\t1]Request\n\t\t\t\t\t2]encrypted software file \n\t\t\t\t\t")
            choice_Reciver_file=int(input("------------------->"))
            if choice_Reciver_file==1:
                print("Select File which is to be Recived ",end=" ")
                print("\n\t\t\t\t\t1]ECU Public Key\n\t\t\t\t\t2]ECU Private Key\n\t\t\t\t\t2]Tester Public Key\n\t\t\t\t\t")
                choice_Reciver_key=int(input("------------------->"))  
                if choice_Reciver_key==1:
                    for file in os.listdir(path):
                        if file.startswith("Receive_ECU_public_key_request"):
                            exFile = os.path.join(path, file)
                            exec(open(exFile).read())
                            break  
                if choice_Reciver_key==2:
                    for file in os.listdir(path):
                        if file.startswith("Receive_ECU_private_key_request"):
                            exFile = os.path.join(path, file)
                            exec(open(exFile).read())
                            break
                if choice_Reciver_key==3:
                    for file in os.listdir(path):
                        if file.startswith("Receive_tester_public_key_request"):
                            exFile = os.path.join(path, file)
                            exec(open(exFile).read())
                            break                                                                                

        elif choice_Reciver==2:
            print("Select File which is to be Recived ",end=" ")
            print("\n\t\t\t\t\t1]Requests \n\t\t\t\t\t2]encrypted software file \n\t\t\t\t\t")
            choice_Reciver_file=int(input("------------------->"))
            if choice_Reciver_file==1:
                for file in os.listdir(path):
                    if file.startswith("Receive_tester_public_key_request"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break            
            elif choice_Reciver_file==2:
                for file in os.listdir(path):
                    if file.startswith("Recive_encryptedsoftware"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break                                                       
    elif(choice==3):
        print("-------------------------------------------------------------------------------------------------------------------")
        for file in os.listdir(path):
            if file.startswith("generate"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())
                break
    elif(choice==4):
        print("-------------------------------------------------------------------------------------------------------------------")
        for file in os.listdir(path):
            if file.startswith("decrypt_software"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())

    elif(choice==5):
        print("-------------------------------------------------------------------------------------------------------------------")
        for file in os.listdir(path):
            if file.startswith("calculat_signature"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())                                
    print("\n\n\n")        