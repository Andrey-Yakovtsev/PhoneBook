from pprint import pprint
from dataset import contacts_list





# class PhoneBook:
#
#     def show_contacts(self):
#         return pprint(contacts_list)
#
#     def add_new_contact(self):
#         return
#
#     def delete_by_phone_number(self):
#         return
#
#     def show_all_favourites(self):
#         return
#
#     def find_by_name_surname(self):
#         return


class Contact:
    def __init__(self, first_name, second_name, phone_number, *w, **Extra_info):
        self.first_name = first_name,
        self.second_name = second_name,
        self.phone_number = phone_number,
        self.is_favourite = 'нет'
        # self.email = email,
        self.Extra_info = Extra_info,

        contacts_list.append(self.__dict__)

    def add_to_favourite(self):
        self.is_favourite = 'да'

    def delete_from_favourite(self):
        self.is_favourite = 'нет'

    def __str__(self):
        return print(f'Имя: {self.first_name}',\
               f'Фамилия: {self.second_name},' \
               f'Телефон: {self.phone_number},' \
               f'В избранных: {self.is_favourite},' \
               f'Дополнительная информация: {self.Extra_info}')



Vasyan = Contact(
    'Vasyan',
    'Chetvertiy',
    '+7565354687323',
    email='asdasd@dsasdfasdf.er',
    telegram='@nekiy',
    facebook='www.facebook.com/whatever'
)
Vasyan.add_to_favourite()

# pprint(Vasyan.__dict__)
# print()
# print()
# pprint(contacts_list)

# PhoneBook.show_contacts(contacts_list)

str(Vasyan)