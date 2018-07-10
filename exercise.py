'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy: 

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop". 

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    def __init__(self):
        super().__init__()
        self.macro = Invoker()
        self.record = False


# ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        if self.record:
            self.macro.add(Command(turtle.forward, arg))
        else:
            turtle.forward(int(arg))

    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        if self.record:
            self.macro.add(Command(turtle.right, arg))
        else:
            turtle.right(int(arg))

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        if self.record:
            self.macro.add(Command(turtle.left, arg))
        else:
            turtle.left(int(arg))

    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        if self.record:
            self.macro.add(Command(turtle.home, arg))
        else:
            turtle.home()

    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        if self.record:
            self.macro.add(Command(turtle.circle, arg))
        else:
            turtle.circle(int(arg))

    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % turtle.position())


    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (turtle.heading(),))


    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        turtle.reset()

    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True

    def do_record(self, arg):
        print('Started recording')
        self.record = True

    def do_stop(self, arg):
        print('Stopped recording')
        self.record = False

    def do_playback(self, arg):
        if self.record is True:
            print('Should stop recording first')
        else:
            self.macro.play()


class Command:
    def __init__(self, command, arg):
        self.command = command
        self.arg = arg

    def execute(self):
        if self.arg:
            self.command(int(self.arg))
        else:
            self.command()


class Invoker:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def play(self):
        for command in self.commands:
            command.execute()


if __name__ == '__main__':
    TurtleShell().cmdloop()
