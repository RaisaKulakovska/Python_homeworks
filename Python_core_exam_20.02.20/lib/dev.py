from lib.employee import Employee


class Developer(Employee):
    def __init__(self, name:str, surname:str, age:int, salary:int, skills:str):
        Employee.__init__(self, name, surname, age, salary)
        self.__skills:str = skills

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, skills):
        self.__skills = skills

    def show_info(self):
        Employee.show_info(self)
        print("Skills: ", self.__skills)

  
