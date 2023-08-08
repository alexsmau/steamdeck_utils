import signal
from xbox360controller import Xbox360Controller

print ('Start program')
print (Xbox360Controller.get_available())

def on_button_pressed(button):
    print ('Button {0} was pressed'.format(button.name))

def on_button_released(button):
    print ('Button {0} was released'.format(button.name))

def on_axis_moved(axis):
    print ('Axis {0} has moved to x:{1} y:{2}'.format(axis.name, axis.x, axis.y))

with Xbox360Controller(0, axis_threshold=0.1) as controller:

    controller.button_a.when_pressed = on_button_pressed
    controller.button_a.when_released = on_button_released

    controller.axis_l.when_moved = on_axis_moved
    controller.axis_r.when_moved = on_axis_moved

    while True:
        #print ('Axis l x:{0} y:{1}'.format(controller.axis_l.x, controller.axis_l.y))
        pass

