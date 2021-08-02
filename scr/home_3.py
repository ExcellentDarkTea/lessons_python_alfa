"""Создать класс FamilyMember, в котором определить:
- поле first_name
- поле family_role (строка, может быть father, mother, son, daughter).
- метод __str__(), возвращающий поле first_name
- метод конструктора, принимающий параметры first_name и family_role и сохраняющий их в одноименные поля объекта.
  Значение first_name перед сохранением должно быть адаптировано с помощью строкового метода capitalize().
"""
class FamilyMembers :
    first_name = ""
    family_role = ""

    def __str__(self):
       return self.first_name.capitalize()

    def __init__(self, name, role):
        self.first_name = name
        self.family_role = role

son = FamilyMembers('Tom', 'son')
mother = FamilyMembers('kaTE', 'mother')

print(f"Вывод только имени через __str__:\n {mother}, {son}")
#print(mother.family_role)

"""
Создать класс Family, в котором определить:
- поле _members как словарь, по умолчанию пустой, хранящий объекты FamilyMember. Ключами в нем будут значения family_role.
- метод  __str__(), возвращающий многострочный текст из данных поля _members, например:
Family:
    - <роль>: <строковое представление мембера с этой ролью>
    - и так по всем ролям
"""

class Family():
    _members = {}

    def __init__(self,FamilyMembers):
        self._members[FamilyMembers.family_role] = FamilyMembers.first_name

    def __str__(self):
        toSTR = ''
        for FamilyMembers.family_role, FamilyMembers.first_name in self._members.items():
            toSTR = toSTR +'\n'+ FamilyMembers.family_role.capitalize() + ' : '+ FamilyMembers.first_name.capitalize()
        return toSTR

m = Family(son)
m = Family(mother)
print(f'\n Вывод словаря построчно со всеми членами семьи:\n {m}')