
import re
class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        # self.balance = start_balance
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу
        self.hystory =[]

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паcпорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.hystory.append(f"Пополнено {amount}")
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < (amount + amount * tax/100):
            self.hystory.append("Недостаточно для перевода")
        else:
            self.__balance -= amount
            self.__balance = self.balance - amount * tax/100
            self.hystory.append(f"Снято {amount} (Комиссия {tax} %)")

    def trans(self, dest, amount: int):
        if self.balance >= amount + amount * tax/100:
            dest.deposit(amount)
            self.withdraw(amount)
            self.hystory.append(f"Перевод -> {dest.name}  {amount} (Комиссия {tax} %)")
            dest.hystory.append(f"Получено <- от {self.name} {amount}")
        else:
            self.hystory.append("Недостаточно для перевода")

regex_pas = "^[0-9\s]*$"
regex_tel = "^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$"

name1 = "Иван";    pas1 = "3230 634563"; tel1 = "+7-900-765-12-34"; bal1 = 1000
name2 = "Алексей"; pas2 = "3232 456124"; tel2 = "+7-901-744-22-99"; bal2 = 200
tax   = 6

if re.match(regex_tel, tel1) and re.match(regex_pas, pas1):
    account1 = Account(name1, pas1, tel1, bal1)
    print(account1.full_info())
else:
    print("Телефон или паспорт указан неверно")
if re.match(regex_tel, tel2) and re.match(regex_pas, pas2):
    account2 = Account(name2, pas2, tel2, bal2)
    print(account2.full_info())
else:
    print("Телефон или паспорт указан неверно")

account2.withdraw(100)
print(account2.full_info())
account2.deposit(1100)
print(account2.full_info())
account2.trans(account1, 20)
account1.trans(account2, 500)
print(account1, account1.hystory)
print(account2, account2.hystory)


