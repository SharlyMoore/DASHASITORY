class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.id}'


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

    def manage_project(self):
        return f'{self.name} управляет в отделе {self.department}'


class Technician(Employee):
    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.name} выполняет техобслуживание по специальности {self.specialization}'


class TechManager(Manager, Technician):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = "Команда:\n"
        for member in self.team:
            team_info += member.get_info() + '\n'
        return team_info


tech_manager = TechManager(name="Эрен", id=1234567, department="ИТ", specialization="айтишник")
manager = Manager(name="Микаса", id=367878, department="PR")
technician = Technician(name="Армин", id=89364562, specialization="техник")

tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
print(tech_manager.get_team_info())
print(manager.manage_project())
print(technician.perform_maintenance())

