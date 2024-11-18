"""
Create a FamilyMember class in which to define:
- first_name 
- family_role (string, can be father, mother, son, daughter).
- __str__() method returning the first_name 
- constructor method, accepting first_name and family_role parameters and saving them to the same-named fields of the object.
  The value of first_name must be adapted using the string method capitalize() before saving.
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

print(f"Name only output via __str__:\n {mother}, {son}")
#print(mother.family_role)

"""
Create a Family class in which to define:
- _members field as a dictionary, empty by default, storing FamilyMember objects. The keys in it will be family_role values.
- A __str__() method that returns multi-line text from the _members field data, such as:
Family:
    - <role>: <string representation of the member with this role>
    - and so on for all roles
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
print(f'\n Dictionary output line by line with all family members:\n {m}')