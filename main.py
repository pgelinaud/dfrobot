def on_button_pressed_a():
    motor.servo(motor.Servos.S1, 30)
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    motor.servo(motor.Servos.S1, 120)
    basic.pause(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)

motor.servo(motor.Servos.S1, 90)
basic.pause(1000)