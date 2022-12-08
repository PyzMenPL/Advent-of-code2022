class Filesystem:
    def __init__(self) -> None:
        self.root = Folder('/')
        # Lista nazw folderów
        self.current_directory = [self.root.name]

    def command(self, command) -> None:
        command = command.split()

        # This is some type of command
        if command[0] == '$' and command[1] == 'cd':
            if command[2] == '..':
                del self.current_directory[-1]
            else:
                self.cd(command[2])

        # Add directory or file if it doesn't exist
        elif command[0] == 'dir' or command[0].isdigit():
            file = None
            if command[0] == 'dir':
                file = Folder(command[1])
            elif command[0].isdigit():
                file = File(command[1], command[0])

            print(file)

            self.root.add(file, self.current_directory[:])

        # If I check for dir and number I don't have to look for the ls command

        else:
            # Won't probably happen tho
            print("Invalid syntax: ", command)

    def cd(self, dst_name=None) -> None:
        if dst_name == '/':
            self.current_directory = []
        else:
            self.current_directory.append(dst_name)

    # TO DO
    @staticmethod
    def sizes(mode):
        if mode == 'get':
            print()
        elif mode == 'update':
            print()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.is_created = False

    def __str__(self):
        return "- {} ({}, size={})".format(self.name, "file", self.size)

    def __repr__(self):
        # Zamiast wypisywać się <class 'str'>, wypisuje się tak jak poniżej
        return "Plik '{}'".format(self.name)


class Folder(File):
    # Folder jest dziedzicem klasy File (bierze od niej imię i rozmiar)
    def __init__(self, name) -> None:
        # To samo co self.name = name i self.size = size
        super().__init__(name=name, size=0)
        self.contains = []

    def __iter__(self):
        # Jeżeli rozpocznie się iteracja
        # Zaczynamy od zera
        self.index = 0
        # Kończymy na ostatnim elemencie z listy
        self.limit = len(self.contains)
        return self

    def __next__(self):
        # Jeżeli zostanie wywołane next() zwiększamy index
        self.index += 1

        # Jeżeli index jest już poza listą, przerywamy iterację
        if self.index == self.limit + 1:
            raise StopIteration

        # Jeżeli index znajduje się w zasięgu listy, zwracamy element listy
        return self.contains[self.index - 1]

    def __str__(self) -> str:
        # Jeżeli potrzebujemy nazwy folderu
        if self.size == 0:
            return "- {} (dir)".format(self.name)
        else:
            return "- {} (dir, size={})".format(self.name, self.size)

    def __repr__(self):
        # Zamiast wypisywać się <class 'str'>, wypisuje się tak jak poniżej
        return "'Folder '{}'".format(self.name)

    def add(self, file, dst_folder_path) -> None:
        # Jeżeli dotrze do folderu docelowego, zapisuje plik.
        # Gdyby warunek nie sprawdzał, czy plik ma nazwę, zostałby jeszcze zapisany w nieodpowiednich miejscach
        if dst_folder_path == [] and file.is_created is False:
            self.contains.append(file)

            # Po dodaniu usuwa nazwę, aby plik nie został ponownie zapisany
            file.is_created = True
            return None

        # Dla każdego elementu w folderze
        for child_folder in self.contains:
            # Sprawdzanie, czy dążenie do folderu zostało zakończone
            if len(dst_folder_path) == 0:
                return None

            # Jeżeli element z listy folderu jest folderem
            if isinstance(child_folder, type(Folder(''))) and child_folder.name == dst_folder_path[0]:
                del dst_folder_path[0]
                child_folder.add(file, dst_folder_path)

    def print(self, depth=0) -> None:
        """Wyświetlenie zawartości podfolderów"""
        # Jeżeli folder jest pusty
        if not self.contains:
            print(depth * '\t', "[Empty]")
            return None

        # Dla każdego elementu w folderze
        for child_folder in self.contains:
            # Wyświetl nazwę z zachowaniem odpowiedniego odstępu
            print(depth * '\t', child_folder)

            # Jeżeli element z listy folderu jest folderem
            if isinstance(child_folder, type(Folder(''))):
                # Wyświetl zawartość podfolderu
                child_folder.print(depth + 1)


with open('input.txt', 'r') as oFile:
    DEBUG = False
    if DEBUG:
        # Creating file system
        fastFS = Filesystem()

        plik = File('plik', 123)

        folder = Folder('Test')
        folder.contains = [plik]

        dir1 = Folder('dir')
        dir1.contains = []

        dir2 = Folder('dir2')
        dir2.contains = [dir1]
        folder.contains.append(dir2)

        fastFS.root.contains = folder.contains

        print("Before:")
        fastFS.root.print()

        fastFS.command('$ cd /')
        fastFS.command('$ cd dir2')
        print(fastFS.current_directory)

        #del fastFS.current_directory[0]

        fastFS.command('dir proba')
        print(fastFS.current_directory)
        print(' ')

        fastFS.command('$ cd dir')
        fastFS.command('420 weed')
        fastFS.command('$ cd ..')
        fastFS.command('$ cd proba')
        fastFS.command('420 surfer')
        print(' ')

        fastFS.command('$ cd ..')
        fastFS.command('2137 JP')
        print(fastFS.current_directory)
        print(' ')

        print("\nAfter:")
        fastFS.root.print()
    else:
        fastFS = Filesystem()
        for line in oFile:
            fastFS.command(line)

        fastFS.root.print()
