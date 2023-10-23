import datetime
from textwrap import wrap


class CreditCard:
    def __init__(self, expiry_month, expiry_year, first_name, last_name, cc_number):
        self.__expiry_month = expiry_month
        self.__expiry_year = expiry_year
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cc_number = cc_number

    def format_expiry_date(self):
        return f"{self.__expiry_month}/{str(self.__expiry_year)[2:4]}"

    def format_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def format_cc_number(self):
        return " ".join(str(self.__cc_number)[i:i+4] for i in range(0, len(str(self.__cc_number)), 4))

    # alternatives for format_cc_number
    # def format_cc_number(self):
    #     cc_list = wrap(self.__cc_number, 4)
    #     return " ".join(cc_list)

    def is_valid(self):
        return datetime.date(self.__expiry_year + 4, self.__expiry_month + 1, 1) >= datetime.date.today()

    def __str__(self):
        return (f"Number: {self.format_cc_number()}  Expiry date: {self.format_expiry_date()}  "
                f"Account holder: {self.format_full_name()}  Is valid: {self.is_valid()}")


if __name__ == "__main__":
    cc1 = CreditCard(10, 2014, "Bob", "Jones", "1234567890123456")
    print(cc1.format_expiry_date())
    print(cc1.format_full_name())
    print(cc1.format_cc_number())
    print(cc1.is_valid())
    print(cc1)

    cc2 = CreditCard(6, 2020, "Benny", "Lao", "0987654312345678")
    print(cc2)
