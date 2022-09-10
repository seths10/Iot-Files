import machine
import time
buzzer_pin = machine.Pin(25, machine.Pin.OUT)
# buzzer = machine.PWM(buzzer_pin)
# buzzer.freq(1047)
# buzzer.duty(50)
# time.sleep(7)
# buzzer.duty(700)
# buzzer.deinit()


C6 = 1047
CS6 = 1109
D6 = 1175
DS6 = 1245
E6 = 1319
F6 = 1397
FS6 = 1480
G6 = 1568
GS6 = 1661
A6 = 1760
AS6 = 1865
B6 = 1976
C7 = 2093
CS7 =2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951


def play(buz_pin, notes, delay, active_duty=50):
    buz = machine.PWM(buz_pin)
    for note in notes:
        if note == 0:
            buz.duty(0)
        else:
            buz.freq(note)
            buz.duty(active_duty)
        time.sleep(delay)
    buz.duty(0)
    buz.deinit()
    

melody1 = [G7, G7, A7, C7, B7, G7, G7, A7, G7, D7, C7, G7, G7, G7, E7, C7, C7, B7, A7, F7, F7, E7, C7, D7, C7]

jingle_bell = [E7, 0, E7, 0, E7, E7, 0, 0,
             E7, 0, E7, 0, E7, E7, 0, 0,
             E7, 0, G7, 0, C7, 0, D7, 0, E7, E7, E7, 0, 0,
             F7, 0, F7, 0, F7, 0, F7, 0, F7, 0,
             E7, 0, E7, 0, E7, 0, E7, 0, D7, 0, D7, 0, E7, 0, D7, D7, 0]

despacito = [C7, C7, C7, 0, B7, B7, B7, 0, A7, 0, E7, 0,
             E7, 0, E7, 0, E7, 0,
             A7, 0, A7, 0, A7, 0, A7, 0, G7, 0, A7, 0, F7, F7, 0, 0,
             F7, 0, F7, 0, F7, 0, F7, 0, A7, 0, A7, 0, A7, 0, A7, 0, B7, 0, C7, 0, G7, 0, 0,
             G7, 0, G7, 0, G7, 0, G7, 0, C7, 0, C7, 0, C7, 0, C7, 0, D7, 0, D7, 0, B7, B7, B7, 0, 0, 0,
             C7, C7, C7, 0, B7, B7, B7, 0, A7, 0, E6, 0]

ciao = [B7, 0, E7, 0, FS7, 0, G7, 0, E7, E7, 0, 0,
        B7, 0, E7, 0, FS7, G7, 0, E7, 0, 0, 0,
        B7, 0, E7, 0, FS7, 0, G7, G7, 0, 0, FS7, E7, 0, G7, G7, 0,
        FS7, E7, 0, B7, B7, 0, B7, B7, 0, B7, B7, 0, 0,
        C7, A7, 0, B7, 0, C7, 0, C7, 0, 0,
        B7, 0, A7, 0, C7, 0, B7, B7, 0,
        A7, 0, G7, 0, FS7, FS7, 0, FS7, 0, B7, 0, FS7, 0, G7, 0, E7]

ghana = [
        C6, C6, 0, 0, G6, 0, G6, 0, G6, 0, G6, 0, G6, G6, 0, 0, 0,
         E6, 0, F6, 0, E6, 0, D6, 0, C6, 0, A6, A6, 0, 0, 0,
         G6, G6, 0, C6, C6, 0, B6, B6, 0, D6, D6, 0, C6, C6, 0, 0, 0, 0,
         C6, C6, 0, 0, G6, 0, G6, 0, G6, 0, G6, 0, G6, G6, 0, 0, 0,
         E6, 0, F6, 0, E6, 0, D6, 0, C6, 0, A6, A6, 0, 0, 0,0,
         G6, G6, 0, C6, C6, 0, B6, B6, 0, D6, D6, 0, C6, C6, 0,
         C7, 0, C7, 0, 0, G6, 0, A6, 0, G6, 0, 0, E6, 0, G6, G6, 0, 0, 0,
         F6, 0, E6, 0, F6, 0, 0, E6, 0, F6, 0, 0, E6, E6, 0, D6, D6, D6, 0, C6, C6, 0, A7, 0,
         G6, G6, 0, C6, C6, 0, B6, B6, 0, D6, D6, 0, C6, C6, 0, 0, 0, 0,
         ]

for i in range(1):
#     play(buzzer_pin, melody1, 0.15)
#     time.sleep(1.5)
#     play(buzzer_pin, jingle_bell, 0.15)
#     time.sleep(1.5)
#     play(buzzer_pin, ciao, 0.15)
#     time.sleep(1.5)
#     play(buzzer_pin, despacito, 0.15)
#     time.sleep(1.5)
    play(buzzer_pin, ghana, 0.19)
    time.sleep(1.5)