class Hospital:

    def __init__(self):
        self.patients= []

    def add_patient(self,Patient_Id,Patient_Name,Patient_Age,Patient_height,Patient_weight,Patient_Gender,Patient_Diagnosis):
        patient = {
            "ID"        : Patient_Id,
            "Name"      : Patient_Name,
            "Age"       : Patient_Age,
            "Height"    : Patient_height,
            "Weight"    : Patient_weight,
            "Gender"    : Patient_Gender,
            "Diagnosis" : Patient_Diagnosis
        }

        self.patients.append(patient)

    def display_patients(self):

        if not self.patients:
            print("No Patients in this Hospital....")

        else:
            for i in self.patients:
                print("Patient ID : ",i['ID'])
                print("Patient Name : ",i['Name'])
                print("Patient Age : ",i['Age'])
                print("Patient Height : ",i['Height']) 
                print("Patient Weight : ",i['Weight']) 
                print("Patient Gender : ",i['Gender'])    
                print("Patient Diagnosis : ",i['Diagnosis'])
                print("     ")

    def search_patient(self,Patient_id):

        for i in self.patients:
            if i['ID'] ==Patient_id:
                print("Patient Found")
                print("Patient ID :",i['ID'])
                print("Patient Name :",i["Name"])
                print("Patient Age : ",i['Age'])
                print("Patient Height : ",i['Height'])
                print("Patient Weight : ",i['Weight'])
                print("Patient Gender : ",i['Gender'])
                print("Patient Diagnosis : ",i['Diagnosis'])
                return
        print("Patient With ID : ",Patient_id," Not Found")

    def delete_patient(self,patient_id):

        for i in self.patients:
            if i['ID'] ==patient_id:
                self.patients.remove[i]
                print("Patient With ID", patient_id," Deleted Sucess fully...")
                return
        print("Patient With ID ",patient_id, " Not Found ")

    def update_patient(self,patient_id,diagnosiss):

        for i in self.patients:
            if i['ID'] == patient_id:
                i['Diagnosis'] = diagnosiss
                print("Patient information updated....")
                return
        print("patient with ID ",patient_id, " Not Found.... ")

main = Hospital()

while True:
    print(".....................WELCOME TO DORIKINANTHA DOCHUKO HOSPITAL....................")
    print("\t\t\t1. ADD A NEW PATIENT : ")
    print("\t\t\t2.DISPLAY ALL PATIENTS : ")
    print("\t\t\t3.SEARCH A PATIENT BY ID : ")
    print("\t\t\t4.DELETE A PATIENT BY ID :  ")
    print("\t\t\t5.UPDATE A PATIENT DIAGNOSIS BY ID: ")
    print("\t\t\t6.EXIT")
    option =input("Enter your option :  ")

    if option== '1':
        Patient_Id= int(input("\t\t\tEnter Patient ID : "))
        Patient_Name= input("\t\t\tEnter Patient Name : ")
        Patient_Age = int(input("\t\t\tEnter Patient Age : "))
        Patient_Height = float(input("\t\t\tEnter Patient Height : "))
        Patient_Weight = int(input("\t\t\tEnter Patient Weight : "))
        Patient_Gender = input("\t\t\tEnter patient Gender     : ")
        Patient_Diagnosis = input("\t\t\tEnter patient Diagnosis  : ")
        main.add_patient(Patient_Id,Patient_Name,Patient_Age,Patient_Height,Patient_Weight,Patient_Gender,Patient_Diagnosis)

    elif option =='2':
        main.display_patients()

    elif option == '3':
        patient_id = int(input("Entet Your Patient ID : "))
        main.search_patient(patient_id)

    elif option == '4':
        patient_id = int(input("Enter Your Patient ID : "))
        main.delete_patient(patient_id)

    elif option == '5':
        patient_id = int(input("Enter Your Patinet ID : "))
        Patient_Diagnosiss = input("Enter Patient Diagnosis's : ")
        main.update_patient(patient_id,Patient_Diagnosiss)

    elif option == '6':
        print(" Thank You... ")
        break

    else:
        print("Invalid option, Please try Again ")

