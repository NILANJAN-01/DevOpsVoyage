'''
FILE_CONTENT: Today is 02-09-2024 Started with Basic Python Scripting 
Let's get your hands dirty in Coding 


'''
class HelloCoder:

    def __init__(self):
        pass
    def startwithpython():
        return "Hello Pyhton developer"
    def startwithjava():
        return "Hello Java developer"
    def ExpectedSalaryForDev(self,experience):
        self.experience = experience
        if experience < 3:
            basesalary = 25000
            print("Base salary is = ", basesalary)        
        elif experience > 3 and self.experience < 10:
            basesalary = 500000
            print("Base salary is = ", basesalary)
        else:
            basesalary = 150000
            print("Base salary is = ", basesalary)
                        
experience_in_year = int(input('Please provide your number of experience =  '))
Nilanjan = HelloCoder().ExpectedSalaryForDev(experience_in_year)
print(Nilanjan)


