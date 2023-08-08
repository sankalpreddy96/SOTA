import os
print("\n\n**************************************ECU**************************************\n\n")
path="C:/Users/Pavithra/OneDrive/Desktop/ECU/ECU/Source Code"
while 1: 
    print("Enter the choice your intersted in:     1]Send \n\t\t\t\t\t2]Recive \n\t\t\t\t\t4]Decryption of software \n\t\t\t\t\t5]Verification of digital signature")
    choice=int(input("------------------->"))
    """Sender part choice"""
    if choice==1:
        print("******************************************************************************************************************")
        print("Send to 2]PKI")
        choice_sender=int(input("------------------->"))
             
        if choice_sender==2:
            print("Select File which is to be sent ",end=" ")
            print("\n\t\t\t\t\t1] Request for ECU Private key" )
            print("\n\t\t\t\t\t2] Request for Tester Public key" )
            choice_sender_file=int(input("------------------->"))
            if choice_sender_file==1:
                for file in os.listdir(path):
                    if file.startswith("Send_ecu_private_rq"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break  
            if choice_sender_file==2:
                for file in os.listdir(path):
                    if file.startswith("send_tester_public_rq"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break  
    """Reciver Part Choice"""                                    
    if choice==2:
        print("******************************************************************************************************************")
        print("Recive from 1]Tester \n\n\t2]PKI") 
        choice_Reciver=int(input("------------------->"))
        if choice_Reciver==1:
            print("Select File which is to be Recived ",end=" ")
            print("\n\t\t\t\t\t1]Receive encrypted software which is appended with signature")
            choice_Reciver_file=int(input("------------------->"))
            if choice_Reciver_file==1:
              for file in os.listdir(path):
                    if file.startswith("Receive_final_data"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break             
        elif choice_Reciver==2:
            print("Select File which is to be Recived ",end=" ")
            print("\n\t\t\t\t\t1] ECU Private Key")
            print("\n\t\t\t\t\t2] tester Public Key")
            choice_Reciver_file=int(input("------------------->"))
            if choice_Reciver_file==1:
              for file in os.listdir(path):
                    if file.startswith("Receive_ECU_private"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break                
            elif choice_Reciver_file==2:
                for file in os.listdir(path):
                    if file.startswith("Receive_tester_public.py"):
                        exFile = os.path.join(path, file)
                        exec(open(exFile).read())
                        break                                                       
    elif(choice==3):
        print("******************************************************************************************************************")
        for file in os.listdir(path):
            if file.startswith("Split_software_sign"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())
                break
    elif(choice==4):
        print("******************************************************************************************************************")
        for file in os.listdir(path):
            if file.startswith("decrpytion_software"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())                
         
    elif(choice==5):
        print("******************************************************************************************************************")
        for file in os.listdir(path):
            if file.startswith("verify_signature"):
                exFile = os.path.join(path, file)
                exec(open(exFile).read())                

                  
    print("\n\n\n")       