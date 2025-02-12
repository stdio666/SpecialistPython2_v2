class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age: int) -> None:
        if type(new_age) ==int and new_age >=1 and new_age <= 100:
            self.age = new_age
        else:
            print(new_age)

    def full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def full_info(self) -> str:
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


# Создадим двух человек:
people1 = People("Иван", "Уткин", 27)
people2 = People("Алексей", "Перов", 35)
people3 = People("Василий", "Быстров", 65)

print(people1.full_info())
print(people2.full_info())
print(people3.full_info())

print("Меняем возраст людей")
people1.change_age(45)
people2.change_age("help")
people2.change_age(-30)

print(people1.full_info())
print(people2.full_info())
print(people3.full_info())
