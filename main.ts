input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    número += -1
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    número = inicial
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    número += 1
})
let número = 0
let inicial = 0
inicial = 5
número = inicial
basic.forever(function on_forever() {
    basic.showNumber(número)
})
