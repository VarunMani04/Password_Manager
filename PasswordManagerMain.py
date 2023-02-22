from PasswordManager import *
import string
from random import randint, shuffle, sample, choices


#Fill in your Main Program Here
manager = PasswordManager('Student', 'FINAL')
manager.add_password('www.gmail.com', 'a_student')
manager.add_password('www.wm.edu', 'WMstudent', criteria = {'max_spec': 2, 'min_upper': 2})
manager.change_password('www.gmail.com', 'FINAL', new_pass = 'update1235')
manager.get_site_info('www.wm.edu')
print(manager)                       