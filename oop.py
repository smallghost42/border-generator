class Create_border(object):
    def __init__(self,list_border,the_text): 
        self.all_border = list_border
        self.text = the_text

    def set_border(self,i):
        self.border = self.all_border[i]

    def get_border(self,j):
        self.set_border(j)
        return self.border

    def top_border(self):
        top_bord = self.get_border(0) + self.get_border(2) * (self.max_len + (len(self.padding) * 2)) + self.get_border(1)
        return top_bord

    def bottom_border(self):
        bottom_bord = self.get_border(4) + self.get_border(2) * (self.max_len + (len(self.padding) * 2)) + self.get_border(5)
        return bottom_bord

    def middle_border(self):
        count = 0
        fin = ''
        current = ''
        for charactere in self.text:
            if charactere == '\n':
                fin = self.get_border(3)
                print(self.get_border(3) + self.padding + current + (' ' * ((self.max_len - count))) + self.padding + fin)
                current = ''
                count = 0
            else:
                current += charactere
                count += 1 

    def print_border(self):
        self.padding = '  '
        self.max_len = 30
        print(self.top_border())
        self.middle_border()
        print(self.bottom_border())

def make_text():
    name = input('enter your name : _')
    age = input('enter your age : _')
    skill = input('what s your skill : _')
    level = input('your curent level : _')

    the_text = 'name : '+ name + '\n' + 'age : ' + age + '\n' + 'skill : ' + skill + '\n' + 'level : ' + '\n'
    return the_text

the_text = make_text()

my_bord = Create_border(['┌','┐','─','│','└','┘'], the_text)
my_bord.print_border()
