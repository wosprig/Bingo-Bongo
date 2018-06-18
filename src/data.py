class Data:

    def __init__(self):
        self.names = {}
        self.all_aliases = {}
        self.ships = {}
        self.ship_aliases = {}
        self.name_list = ""
        self.ship_list = ""
        self.init_ships()
        self.init_names()

    def init_names(self):
        file = open("names.dat", 'r')
        temp = file.read().split('\n')
        for person in temp:
            components = person.split('\t')
            name = components[0]
            alias_list = name
            self.names[name.lower()] = name
            if len(components) > 1:
                for alias in components[1][1:len(components[1]) - 1].split(","):
                    alias_list += "\n" + alias
                    self.names[alias.lower()] = name
            self.all_aliases[name.lower()] = alias_list
            self.name_list += name + "\n"

    def init_ships(self):
        file = open("ships.dat", 'r')
        temp = file.read().split('\n')
        for relationship in temp:
            components = relationship.split('\t')
            name = components[0]
            alias_list = name
            self.ships[name.lower()] = name
            if len(components) > 1:
                for alias in components[1][1:len(components[1]) - 1].split(","):
                    alias_list += "\n" + alias
                    self.ships[alias.lower()] = name
            self.ship_aliases[name.lower()] = alias_list
            self.ship_list += name + "\n"

    def getaliases(self, arg):
        if arg in self.names:
            name = self.names.get(arg.lower())
            return self.all_aliases.get(name.lower())
        elif arg in self.ships:
            name = self.ships.get(arg.lower())
            return self.ship_aliases.get(name.lower())
