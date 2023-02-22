import random
import string
from random import randint, shuffle, sample, choices
import pandas as pd

class PasswordManager:

    def __init__(self, name, master_pw):
        self.__passwords = pd.DataFrame(columns = ['Site','Username','Password'])
        #self.__passwords.columns = ['Site','Username','Password'] 
        self.__passwords.set_index('Site', inplace = True)
        self.__name = name #store name of the user
        self.__master_pw = master_pw #store master password
    
    def __password_specs(self, length = 14, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
#update this code so that it works with the max_spec argument
#it is otherwise correct
#HINT: you only need to change one line of code in this implementation to
#do this, and it is the FIRST LINE
#Or you can add a few lines, but they go before the FIRST LINE
        if max_spec > (length - min_num - min_upper):
            num_sc  = randint(min_spec, max_spec)
        elif max_spec <= (length - min_num - min_upper):
            num_sc = randint(min_spec, max_spec)
        #num_sc = randint(min_spec, length - min_num - min_upper) 
        num_num = randint(min_num, length - num_sc  - min_upper)
        num_upper = randint(min_upper, length - num_sc - num_num)
        num_lower = length - (num_sc + num_num + num_upper)
        return [num_sc, num_num, num_upper, num_lower]       
  
    def __password_gen(self, criteria = None,length = 14, spec_char = '@!&', repeat = True, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
#FILL IN THIS PART with your code to make use of criteria
#Check if criteria contains information, if so, use that the update the parameters
#It may not have an entry for every parameter, just update for the ones it has
#This should be VERY SIMPLE but may take several lines
        if criteria != None: 
            for key in criteria: 
                if key == 'length':
                    length = criteria[key]
                if key == 'spec_char': 
                    spec_char = criteria[key]
                if key == 'repeat':
                    repeat = criteria[key]
                if key == 'min_spec':
                    min_spec = criteria[key]
                if key == 'max_spec':
                    max_spec = criteria[key]
                if key == 'min_num':
                    min_num = criteria[key]
                if key == 'min_upper':
                    min_upper = criteria[key]
#Next, we will help the user out a little bit here with some error checking
#The two lines of code below are correct, do not change them
        if(max_spec < min_spec): 
            max_spec = min_spec 
#Code below is algorithmically correct, you must change it so that it works in the context of this
#Object and its methods, these are tiny/minimal changes, you should not have to 
#Move any lines, add any lines or delete any lines, or re-write much at all
#If you are changing several lines (like >2), or are adding or deleting large pieces of code
#You are doing it wrong, DO NOT OVERTHINK THIS
        required = sum([min_spec, min_num, min_upper]) 
        if required <= length and (repeat or len(spec_char)>=min_spec): 
            specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
            if(repeat): 
                password = random.choices(string.ascii_lowercase, k=specs[3]) + random.choices(string.ascii_uppercase, k=specs[2]) + random.choices(string.digits, k=specs[1]) + random.choices(spec_char, k=specs[0])
            else:
                while specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase) or specs[3] > len(string.ascii_lowercase):
                    specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
                password = random.sample(string.ascii_lowercase, k=specs[3]) + random.sample(string.ascii_uppercase, k=specs[2]) + random.sample(string.digits, k=specs[1]) + random.sample(spec_char, k=specs[0])
            shuffle(password) 
            return ''.join(password)
        
    def add_password(self, site, username, criteria = None):
        if site not in self.__passwords.index:
            self.__password = self.__password_gen(criteria)
        if self.__password == None:
            print("Invalid Specifications")
        else: 
            self.__passwords.loc[site] = [username, self.__password]


    def validate(self, mp):

        return True if self.__master_pw == mp else False

    def change_password(self, site, master_pass, new_pass = None, criteria = None):
        if self.validate(master_pass) == False: 
            print("Invalid Master Password!")
            return self.validate(master_pass)
        else: 
            if site in self.__passwords.index:
                if new_pass != None: 
                    self.__passwords[site,"Password"] = new_pass
                else: 
                    diff_pass = self.__password_gen(criteria) 
                    for item in self.__passwords['Password']:
                        if(diff_pass == item):
                            print("Invalid Criteria!")
                            return False 
                        else: 
                            self.__passwords.loc[site,"Password"] = new_pass
            else: 
                print("Site does not exist!")
                return False
            
    def remove_site(self, site):
        if site in self.__passwords.index:
            self.__passwords.drop(site, inplace = True) 

    def get_site_info(self, site):
        if site in self.__passwords.index:
            return list(self.__passwords.loc[self.__passwords.index == site].iloc[0])

    def get_name(self):
        return self.__name 

    def get_site_list(self):
        return list(self.__passwords.index)
        
    def __str__(self):

        string = ""
        for item in string: 
            string += item
        return ("Site stored for " + self.__name + ":\n" + string)

