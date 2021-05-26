# -*- coding: utf-8 -*-
"""
Created on Thu May 20 05:49:28 2021

@author: Gautham
"""

class Employee:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__base_annual_salary = 0
        self.__bonus_percentage = 0
    
    # Methods
    def get_monthly_gross(self):
        return self.__base_annual_salary/12
    
    def get_standard_annual_bonus_amount(self):
        return self.__base_annual_salary*(self.__bonus_percentage/100)
    
    def __get_employee_id(self):
        return "111-222-333"

    def get_emp_id(self):
        return self.__get_employee_id()
    
    # Getters
    def get_base_annual_salary(self):
        return self.__base_annual_salary
    
    def get_bonus_percentage(self):
        return self.__bonus_percentage
    
    # Setters
    def set_base_annual_salary(self, base_annual_salary):
        if 45000.00 <= base_annual_salary <= 120000.00:
            self.__base_annual_salary = base_annual_salary
        else:
            print("Annual base salary must be between 45K and 120K!")
    
    def set_bonus_percentage(self, bonus_percentage):
        if 0.05 <= bonus_percentage <= .21:
            self.__bonus_percentage = bonus_percentage
        else:
            print("Bonus percentage must be between 5% (.05) and 21% (.21)!")
    
def main():
    print("Hello from main()!")
    
    employee1 = Employee("Kara", "Smith")
    employee1.set_bonus_percentage(0.1)
    employee1.set_base_annual_salary(50000.00)
    
    monthly_gross_pay = employee1.get_monthly_gross()
    standard_annual_bonus = employee1.get_standard_annual_bonus_amount()
    
        
    print("Annual Salary: {:.2f}".format(employee1.get_base_annual_salary()))
    print("Monthly gross Salary: {:.2f}".format(monthly_gross_pay))
    print("Annual Standard Bonus: {:.2f}".format(standard_annual_bonus))
    
if __name__ == '__main__':
    main()
