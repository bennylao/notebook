import datetime


class CreditCard:

    def __init__(self, expiry_month, expiry_year, first_name, last_name, cc_number):
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.first_name = first_name
        self.last_name = last_name
        self.cc_number = cc_number

    def __str__(self):
        return f"Number: {self.format_cc_number()} \nExpiry date: {self.format_expiry_date()}\nAccount holder: " \
               f"{self.format_full_name()}\nIs valid: {self.is_valid()}"

    def format_expiry_date(self):
        formatted = str(self.expiry_month) + '/' + str(self.expiry_year)[-2] + str(self.expiry_year)[-1]
        return formatted

    def format_full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def format_cc_number(self):
        """

        :return: formatted credit card no. string with space every 4 numbers.
        """
        formatted = self.cc_number
        return ' '.join(formatted[i: i + 4] for i in range(0, len(formatted), 4))

    def is_valid(self):
        """

        :return: False if expired and True if date still valid.
        """
        formatted_expiry = datetime.datetime.strptime(self.format_expiry_date(), '%m/%y')
        if formatted_expiry > datetime.datetime.now():
            return True
        else:
            return False


cc1 = CreditCard(10, 2014, 'Bob', 'Jones', '5763564651')
cc2 = CreditCard(11, 2020, 'Mary', 'Smith','7874546549')

print(cc1.format_expiry_date())
print(cc1.format_full_name())
print(cc1.format_cc_number())
print(cc1.is_valid())
print(cc2.is_valid())

print(cc2.__str__())
print(cc1.__str__())

