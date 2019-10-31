#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:12:44 2019

@author: naveen
"""
"""
119. Program to do single inheritance, multiple inheritance and multilevel 
inheritance (by inputting employee name, id, gender, stream, year, address, 
contact number etc)
"""
class Employee:
    def __init__(self,name,id_,gender):
        self.name=name
        self.id_=id_
        self.gender=gender
    def input_data(self,name,id_,gen):
        """
        Method To input data
        Arguments:
            name,id_,gen
        
        """
        self.name=name
        self.id_=id_
        self.gender=gen
    
    def show(self):
        """
        Method shows employee details
        """
        print("Name :",self.name)
        print("Id :",self.id_)
        print("Gender :",self.gender)
        
class Employee_pro(Employee):
    def __init__(self,name,id_,gender,stream,year):
        Employee.__init__(self,name,id_,gender)#getting __init__ from parent class Employee
        self.stream=stream
        self.year=year
    def show_pro(self):
        print("Stream :",self.stream)
        print("Year :",self.year)
   
class Employee_addr(Employee):
    def __init__(self,name,id_,gender,addr,contact):
        Employee.__init__(self,name,id_,gender)#getting __init__() consttructor from Employee class
        self.addr=addr
        self.contact=contact
    def show_addr(self):
        print("Address:\n",self.addr)
        print("Contact No:",self.contact)
    
        
nm=input("Enter Employee Details:\nName:")
gn=int(input("Gender:\n1.M\n2.F\n3.OTH\n:"))
iden=input("Id:")
gen=""
if gn==1:
    gen="M"
elif gn==2:
    gen="F"
elif gen==3:
    gen="OTH"

#e1=Employee(nm,iden,gen)#makes an instance of employee class
#e1.show()

strc=int(input("Stream\n1.Development\n2.Implementation\n3.Testing\n:"))
yr=int(input("Year of Join:"))
stream_=""
if strc==1:
    stream_="Development"
elif strc==2:
    stream_="Implemetation"
elif strc==3:
    stream_="Testing"
"""
e_pro=Employee_pro('Roy','S35','M',stream_,yr)#instance of Employee_pro
e_pro.show()
e_pro.show_pro()
"""
address=""
addr_1=input("House Name/No:")
addr_2=input("Street :")
addr_3=input("City:")
addr_4=input("District:")
addr_5=input("State:")
addr_6=int(input("PIN:"))
address+=addr_1+'\n'+addr_2+'\n'+addr_3+'\n'+addr_4+'\n'+addr_5+'-'+str(addr_6)
ph=int(input("Contact no:"))
emp_addr=Employee_addr('Roy','S35','M',address,ph)#instance of Employee_addr
emp_addr.show()
emp_addr.show_addr()



    
    
