class Person:
    patient_no = 0
    patient_data = {}

    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

    def __str__(self):
        return "Name:{}\nGender:{}\nAge:{}".format(self.name, self.gender, self.age)


# Write your code here
class Patient(Person):
    def __init__(self, n, g, a, r="Unknown"):
        super().__init__(n, g, a)
        Patient.patient_no += 1
        self.registration_date = r
        if r != "Unknown":
            self.patient_id = str(Patient.patient_no) + self.name.split()[0] + r[-2:]
        else:
            self.patient_id = str(Patient.patient_no) + self.name.split()[0]
        # print(self.patient_id)
        Patient.patient_data[self.patient_id] = [
            self.name,
            self.gender,
            self.age,
            self.registration_date,
        ]

    def __str__(self):
        return (
            "Patient_ID: {}\n".format(self.patient_id)
            + super().__str__()
            + "\nRegistered Date: {}\nNumber of Patients: {}".format(
                self.registration_date, Patient.patient_no
            )
        )

    def createPatient(n, g, a, r="Unknown"):
        x = Patient(n, g, a, r)
        return x


print(Person.patient_data)
print("####################")
sam = Patient("Samuel Brown", "male", 32)
print("=========Print Details of a Patient=========")
print(sam)
print("####################")
tom = Patient("Tom Brown", "male", 32, "2nd December, 2017")
print("=========Print Details of a Patient=========")
print(tom)
print("####################")
sara = Patient("Sara Fernandes", "female", 48, "18th April, 2016")
print("=========Print Details of a Patient=========")
print(sara)
print("####################")
richard = Patient.createPatient("Richard Brown", "male", 32, "2nd December, 2017")
print("=========Print Details of a Patient=========")
print(richard)
print("####################")
print(Person.patient_data)

"""
Output:
{}
####################
=========Print Details of a Patient=========
Patient_ID: 1Samuel
Name: Samuel Brown
Gender: male
Age: 32
Registered Date: Unknown
Number of Patients: 1
####################
=========Print Details of a Patient=========
Patient_ID: 2Tom17
Name: Tom Brown
Gender: male
Age: 32
Registered Date: 2nd December, 2017
Number of Patients: 2
####################
=========Print Details of a Patient=========
Patient_ID: 3Sara16
Name: Sara Fernandes
Gender: female
Age: 48
Registered Date: 18th April, 2016
Number of Patients: 3
####################
=========Print Details of a Patient=========
Patient_ID: 4Richard17
Name: Richard Brown
Gender: male
Age: 32
Registered Date: 2nd December, 2017
Number of Patients: 4
####################
{'1Samuel': ['Samuel Brown', 'male', 32, 'Unknown'],  '3Tom17': ['Tom Brown', 'male', 32, '2nd December, 2017'], '3Sara16': ['Sara Fernandes', 'female', 48, '18th April, 2016'], '4Richard17': ['Richard Brown', 'male', 32, '2nd December,2017']}
"""
