from Chef import Chef
from ChineseChef import ChineseChef
from Student import Student

student1 = Student('John', 23)
student2 = Student('Geverton', 24)

print(student1)
print(student1.name)
print(student1.age)
print(f'Is Geverton dumb? {student2.is_dumb()}')

chef = Chef('Dan')
chef.make_rice()

chineseChef = ChineseChef('Yu')
chineseChef.make_rice()
chineseChef.make_beans()
