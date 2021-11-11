#Handler 11/9/21 Kyle Tennison

import movements

filename = "current.key"

class command:
    pass


def main():

    movements.update()

    #Read Command File
    with open("current.key", 'r') as command.file:
        command.raw = command.file.read().strip()
        if command.raw == "":
            return
        command.command = movements.process(command.raw)
    print(f"Current command: {command.command}")

    if command.command[0] == 'walk': movements.walk(command.command[1])
    elif command.command[0] == 'run': movements.run(command.command[1])
    elif command.command[0] == 'stopwalk': movements.stopwalk()
    elif command.command[0] == 'stepW': movements.step.forward()
    elif command.command[0] == 'stepA': movements.step.left()
    elif command.command[0] == 'stepD': movements.step.right()
    elif command.command[0] == 'stepS': movements.step.backward()
    elif command.command[0] == 'jump': movements.jump()
    elif command.command[0] == 'lookR': movements.look.right(command.command[1])
    elif command.command[0] == 'lookL': movements.look.left(command.command[1])
    elif command.command[0] == 'lookU': movements.look.up(command.command[1])
    elif command.command[0] == 'lookD': movements.look.down(command.command[1])
    elif command.command[0] == 'stop': movements.stop()
    elif command.command[0] == 'eat': movements.eat()
    elif command.command[0] == 'mine': movements.mine(command.command[1])
    elif command.command[0] == 'stopmine': movements.stopmine()
    elif command.command[0] == 'place': movements.place()
    elif command.command[0] == 'hit': movements.hit()
    elif command.command[0] == 'hotbar': movements.hotbar(command.command[1])

    with open("current.key", 'w') as command.file:
        command.file.write('')





if __name__ == "__main__":

    while True:
        try:
            main()
        except Exception as e:
            print("======== error:", e)
            with open("current.key", 'w') as command.file:
                command.file.write('')


"""

commands = {
    'stop'      : False,
    'eat'       : False,
    'mine'      : True,
    'stopmine'  : False,
    'place'     : False,
    'hit'       : False,
    'hotbar'    : True
}
"""
