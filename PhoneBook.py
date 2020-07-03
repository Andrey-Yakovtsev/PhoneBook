from pprint import pprint
# from dataset import contacts_list


class Contact:
    # contacts_list = []
    def __init__(self, first_name, second_name, phone_number=str, is_favourite='нет', **Extra_info):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.is_favourite = is_favourite
        self.Extra_info = Extra_info
        # self.contacts_list.append(self.__dict__)

    def add_to_favourite(self):
        self.is_favourite = 'да'

    def delete_from_favourite(self):
        self.is_favourite = 'нет'



    def __str__(self):
        return f'Имя: {self.first_name}\n' \
               f'Фамилия: {self.second_name}\n' \
               f'Телефон: {self.phone_number}\n' \
               f'В избранных: {self.is_favourite}\n' \
               f'Дополнительная информация: \n\t' \
               f'e-mail: {self.Extra_info["email"]}\n\t' \
               f'telegram: {self.Extra_info["telegram"]}\n\t' \
               f'facebook: {self.Extra_info["facebook"]}'

Vasyan = Contact(
    'Vasyan',
    'Chetvertiy',
    '+7565354687323',
    email='asdasd@dsasdfasdf.er',
    telegram='@nekiy',
    facebook='www.facebook.com/whatever'
)
Petka = Contact(
    'Пятый',
    'Петька',
    '+7555555555',
    email='555@fifth.com',
    telegram='@555',
    facebook='www.facebook.com/fivestar'
)
Vasyan.add_to_favourite()
# print(Vasyan)
# print(Petka)

class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.contacts_list = []

    def show_contacts(self):
        for item in self.contacts_list:
            pprint(item)

    def add_new_contact(self, Contact):
        self.contacts_list.append(Contact)
        # self.contacts_list.append(self.__dict__)

MyTopContacts = PhoneBook
MyTopContacts.add_new_contact(Petka)
# MyTopContacts.show_contacts()