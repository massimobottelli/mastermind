from pybricks.pupdevices import Motor
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port, Color, Direction
from pybricks.tools import wait
from pybricks.hubs import MoveHub

# Initialize devices
hub = MoveHub()
sensor = ColorDistanceSensor(Port.C)
flag1_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
flag2_motor = Motor(Port.B, Direction.CLOCKWISE)
drawer_motor = Motor(Port.D)

# Initialize random seed
_rand = hub.battery.voltage() + hub.battery.current()

# constants
DRAWER_SPEED = 400
DRAWER_STEP_ANGLE = 145
FLAG_SPEED = 200
FLAG_STEP_ANGLE = 90
PAUSE_COLOR = 500
PAUSE_SEQUENCE = 5000
DISTANCE = 20

# Initialize score
score = [0, 0, 0]

# Set reset positions
flag1_motor.reset_angle(0)
flag2_motor.reset_angle(0)
drawer_motor.reset_angle(0)

# Function to generate random integer
def randint(a, b):
    global _rand
    _rand = 75 * _rand % 65537  # Lehmer
    return _rand * (b - a + 1) // 65537 + a

# Function to read user color
def read_color():
    color = sensor.color()
    return str(color)

# Function to provide feedback to user
def feedback_flag(flag, dir):
    flag.run_angle(FLAG_SPEED, FLAG_STEP_ANGLE)
    wait(PAUSE_COLOR)
    flag.run_target(FLAG_SPEED, 0)

# At startup, generate random sequence
random_colors = []
while len(random_colors) < 3:
    random = randint(1, 4)
    if random == 1: random = "Color.RED"
    if random == 2: random = "Color.GREEN"
    if random == 3: random = "Color.BLUE"
    if random == 4: random = "Color.YELLOW"
    # Append color only if not already in random sequence
    if random not in random_colors:
        random_colors.append(random)
print ("Random sequence: ", random_colors) #debug

# Loop until user inserts the correct sequence
while (score != [1, 1, 1]):

    # Wait until the drawer is placed under the sensor
    while (sensor.distance() > DISTANCE):
        pass
    wait(PAUSE_COLOR * 4)
    
    # Move to left 
    drawer_motor.run_angle(DRAWER_SPEED, DRAWER_STEP_ANGLE)
    wait(PAUSE_COLOR)

    # Loop to check user colors
    for i in range(0, 3):
        # Read user color
        user_color = read_color()
        if user_color == random_colors[i]:
            # Correct color
            print (user_color, "correct color!") #debug
            feedback_flag (flag1_motor, -1)
            score[i] = 1

        elif user_color in random_colors:
            # Color present but in different position
            print (user_color, "present in different position") #debug
            feedback_flag (flag2_motor, 1)

        else:
            # Color not present
            print (user_color, "not present") #debug

        # Move to next color
        dir = 1 if i == 2 else -1
        drawer_motor.run_angle(DRAWER_SPEED, dir * DRAWER_STEP_ANGLE)
        wait(PAUSE_COLOR)

    # If all colors are correct, user wins
    if score == [1, 1, 1]:
        print ("YOU WIN!")
        break
    else:
        print ("Try again")
        wait(PAUSE_SEQUENCE)

    # Reset position
    drawer_motor.run_target(DRAWER_SPEED, 0)


