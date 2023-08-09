#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 04:46:23 2023

@author: Dilip Kumar
"""

#Everything in python is an object

# x = 1

# # help(x)
# # dir(x)


# y = [1, 2, 3]
# # help(y)
# #dir(y)

# z = {'a': 1}
# help(z)
# dir(z)



# class Patient(object):
#     '''Medical Center Patient'''
#     pass
    

class Patient(object):
    '''
    Patient Records
    Attributes
    ----------
    name: Patient Name
    age: Patient Age
    conditions: list of existing condtion or other informations
    '''
    status = 'patient'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []
        
    def getDetails(self):
        print(f'Patient record: {self.name}, {self.age} years. ' \
              f'more about patient: {self.conditions}')
        
    def addInformation(self, information):
        self.conditions.append(information)
        
        
        
        



# dia = Patient('Dia Ramesh', 21)
# dia.addInformation('Eye Infection')
# dia.addInformation('From Ahmedabad')
# dia.getDetails()


class Infant(Patient):
    '''Patent under 2 years'''
    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)
        
    def addVac(self, vaccine):
        self.vaccinations.append(vaccine)
    
    def getDetails(self):
        print(f'Patient Record: {self.name}, {self.age} years. '\
              f'The patient has had {self.vaccinations} vaccines. '\
             f'more about {self.name}: {self.conditions}. '\
            f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
            
            
            
amir = Infant("Amir Adami", 1)
amir.addInformation("Bangalore")
amir.addInformation("5 KG")
amir.addVac("MMR")
amir.getDetails()

print()
steve = Patient('Steve Hughes', 48)
steve.addInformation('Ear Infection')
steve.addInformation('High BP')
steve.addInformation('From Banglore')
steve.getDetails()