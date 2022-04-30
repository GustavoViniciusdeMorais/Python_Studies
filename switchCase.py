class Switch():
    _print_text ="result: {}"

    def __call__(self, chioce):
        return getattr(self, choice, self.default)()
    
    def sum(self):
        a = input('a:')
        b = input('b:')
        result = int(a) + int(b)
        print(self._print_text.format(result))

    def sub(self):
        a = input('a:')
        b = input('b:')
        result = int(a) - int(b)
        print(self._print_text.format(result))
    
    def default(self):
        print("Invalid option")

choice = input('Enter option (sum, sub):')
switch = Switch()
switch(choice)