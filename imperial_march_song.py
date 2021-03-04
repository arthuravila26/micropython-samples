from machine import PWM, Pin
from time import sleep

MusicNotes = {"B0": 31, "C1": 33,"CS1": 35,"D1": 37,"DS1": 39,"E1": 41,"F1": 44,"FS1": 46,"G1": 49,"GS1": 52,"A1": 55,"AS1": 58,"B1": 62,
"C2": 65,"CS2": 69,"D2": 73,"DS2": 78,"E2": 82,"F2": 87,"FS2": 93,"G2": 98,"GS2": 104,"A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,
"D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,"C4": 262,"CS4": 277,"D4": 294,
"DS4": 311,"E4": 330,"F4": 349,"FS4": 370,"G4": 392,"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,"C5": 523,"CS5": 554,"D5": 587,"DS5": 622,
"E5": 659,"F5": 698,"FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,"C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1324,
"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,"A6": 1760,"AS6": 1865,"B6": 1976,"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,
"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,"AS7": 3729,"B7": 3951,"C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978}

#Notes for imperial March
#imperial_march = ["A3","A3","A3","F3","C4","A3","F3","C4","A3","E4","E4","E4","F4",
#        "C4","GS3","F3","C4","A3", "A4", "A3", "A3", "A4", "GS4", "G4", "FS4","E4", "F4","AS3","DS4","D4","CS4","C4","B3","C4"]

speaker = PWM(Pin(15))
def playnote(Note, Duration):
    sleep(1/20)
    speaker.duty_u16(1500)    
    speaker.freq(MusicNotes[Note])
    sleep(Duration)

playnote('A3', 1/2)
playnote('A3', 1/2)
playnote('A3', 1/2)
playnote('F3', 1/3)
playnote('C4', 1/6)
playnote('A3', 1/2)
playnote('F3', 1/3)
playnote('C4', 1/6)
playnote('A3', 1/2)
sleep(1/2)
playnote('E4', 1/2)
playnote('E4', 1/2)
playnote('E4', 1/2)
playnote('F4', 1/3)
playnote('C4', 1/6)
playnote('GS3', 1/2)
playnote('F3', 1/3)
playnote('C4', 1/6)
playnote('A3', 1/2)
sleep(1/2)
playnote('A4', 1/2)
playnote('A3', 1/3)
playnote('A3', 1/6)
playnote('A4', 1/2)
playnote('GS4', 1/3)
playnote('G4', 1/6)
playnote('FS4', 1/10)
playnote('E4', 1/10)
playnote('F4', 1/10)
sleep(1/2)
playnote('AS3', 1/6)
playnote('DS4', 1/2)
playnote('D4', 1/3)
playnote('CS4', 1/6)
playnote('C4', 1/10)
playnote('B3', 1/10)
playnote('C4', 1/10)
speaker.duty_u16(0)
