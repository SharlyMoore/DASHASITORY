class Employee:
    def __init__(self, a_arg, **kwargs):
        self.a_arg = a_arg
        self.name = name
        self.id_ = id_

    def get_info(self):
        return f'Имя сотрудника: {self.name}, id: {self.id_}'

class Manager(Employee):
    def __init__(self, name, id_, department):
        Employee.__init__(self, name, id_)
        self.department = department

    def manage_project(self):
        return f'{self.name} управляет в отделе {self.department}'

class Technician(Employee):
    def __init__(self, name, id_, specialization):
        Employee.__init__(self, name, id_)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.name} выполняет техническое обслуживание по специальности {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, id_, department, specialization):
        Manager.__init__(self, name, id_, department)
        Technician.__init__(self, name, id_, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = 'Сотрудники:\n'
        for person in self.team:
            team_info += person.get_info() + '\n'
        return team_info

tech_manager = TechManager('Эрен', 234652, "IT", "Айтишник")
manager = Manager('Армин', 245289579, 'Менеджер')
technician = Technician('Микаса', 7486785, 'Техник')

tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
print(tech_manager.get_team_info())


''' print(tech_manager.get_info(), tech_manager.manage_project(), tech_manager.perform_maintenance(), tech_manager.get_team_info(), sep="\n")
    print(manager.get_info(), manager.manage_project(), sep="\n")
    print(technician.get_info(), technician.perform_maintenance(), sep="\n")'''
