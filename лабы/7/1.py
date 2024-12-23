class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.employee_id}'


class Manager(Employee):
    def __init__(self, name, employee_id, department, **kwargs):
        super().__init__(name=name, employee_id=employee_id, **kwargs)
        self.department = department

    def manage_project(self):
        return f'{self.name} управляет проектом в отделе {self.department}'


class Technician(Employee):
    def __init__(self, name, employee_id,specialization):
        super().__init__(name, employee_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.name} выполняет техническое обслуживание по специальности {self.specialization}'


class TechManager(Manager, Technician):
    def __init__(self, name, employee_id,department, specialization, **kwargs):
        super().__init__(name=name, employee_id=employee_id, department=department,specialization=specialization, **kwargs)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = "Команда:\n"
        for member in self.team:
            team_info += member.get_info() + '\n'
        return team_info


if __name__ == "__main__":
    tech_manager = TechManager(name="Иван", employee_id=1, department="ИТ", specialization="Системный администратор")
    manager = Manager(name="Мария", employee_id=2, department="Маркетинг")
    technician = Technician(name="Петр", employee_id=3, specialization="Электрик")

    tech_manager.add_employee(manager)
    tech_manager.add_employee(technician)

    print(tech_manager.get_info(), tech_manager.manage_project(), tech_manager.perform_maintenance(), tech_manager.get_team_info(), sep="\n")
    print(manager.get_info(), manager.manage_project(), sep="\n")
    print(technician.get_info(), technician.perform_maintenance(), sep="\n")

    print(TechManager.__mro__)
