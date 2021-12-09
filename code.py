import board
import digitalio

# Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set the internal resistor to pull-up

# Configure the internal GPIO connected to GP18 as a digital output
plant = digitalio.DigitalInOut(board.GP18)
plant.direction = digitalio.Direction.OUTPUT
plant.value = 0

# Configure the internal GPIO connected to GP18 as a digital output
w_light = digitalio.DigitalInOut(board.GP16)
w_light.direction = digitalio.Direction.OUTPUT
w_light.value = 0

# Print a message on the serial console
print('Hello there! My LED is controlled by the button.')

state = 0

def statefunction(state):
    if state == 0:
        state = 1
        plant = True
        w_light = 0
        print('Turning red and blue lights on!')
    elif state == 1:
        state = 2
        plant = True
        w_light = True
        print('Turning white lights on!')
    else:
        state = 0
        plant = False
        w_light = False
        print('Turning all lights off!')
    return (state, plant, w_light)

# Loop so the code runs continuously
while True:
    
    if button.value == False:
        state, plant.value, w_light.value = statefunction(state)
        
        while button.value == False:
            pass