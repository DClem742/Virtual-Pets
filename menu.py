class Menu:
    def __init__(self, prompt_text):
        self.prompt_text = prompt_text
    
    def get_choice(self, choice_list):
        return self.get_user_choice(choice_list)
        

    def print_menu_error(self):
        print("That was not a valid choice. Try again. \n\n\n")

    def choices_to_string(self, choice_list):
        choice_string = ""
        num = 1
        for choice in choice_list:
            choice_string += "%d: %s\n" % (num, choice)
            num += 1
        choice_string += self.prompt_text
        return choice_string
    
    def get_user_choice(self, choice_list):
        choice = -1
        choice_string = self.choices_to_string(choice_list)
        while choice == -1:
            try:
                choice = int(input(choice_string))
                if choice <= 0 or choice > len(choice_list):
                    raise ValueError
            except ValueError:
                self.print_menu_error()
        return choice