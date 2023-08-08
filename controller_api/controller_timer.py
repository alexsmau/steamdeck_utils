import time
from xbox360controller import Xbox360Controller


# def on_button_pressed(button):
#    print('Button {0} was pressed'.format(button.name))


# def on_button_released(button):
#    print('Button {0} was released'.format(button.name))


# def on_axis_moved(axis):
#    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

try:
    with Xbox360Controller(0, axis_threshold=0.1) as controller:

        # controller.info()

        # Button A events
        # controller.button_a.when_pressed = on_button_pressed
        # controller.button_a.when_released = on_button_released

        # Left and right axis move event
        # controller.axis_l.when_moved = on_axis_moved
        # controller.axis_r.when_moved = on_axis_moved

        while True:
            axisL = "axis left x={0:.3f} y={1:.3f}".format(
                controller.axis_l.x, controller.axis_l.y)
            print(axisL)
            time.sleep(1)
except KeyboardInterrupt:
    pass
