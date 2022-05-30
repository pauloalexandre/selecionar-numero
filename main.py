def on_button_pressed_a():
    global número
    número += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global número
    número = inicial
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global número
    número += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

número = 0
inicial = 0
inicial = 5
número = inicial

def on_forever():
    basic.show_number(número)
basic.forever(on_forever)
