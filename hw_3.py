class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Я учился с Айсулуу в группе {self.group}.")

        if self.higher_education:
            print("У меня есть высшее образование.")
        else:
            print("У меня нет высшего образования.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Мое хобби {self.hobby}.")

        if self.higher_education:
            print("У меня есть высшее образование.")
        else:
            print("У меня нет высшего образования.")

classmate1 = Classmate("Алибек", "15.05.2002", "студент", True, "A-1")
classmate2 = Classmate("Алина", "10.03.2003", "студент", True, "A-1")

friend1 = Friend("Жоомарт", "01.01.2000", "официант", False, "футбол")
friend2 = Friend("Айжан", "20.07.2001", "дизайнер", True, "рисование")

classmate1.introduce()
classmate2.introduce()

friend1.introduce()
friend2.introduce()