from MotorModule import Motor
import keyPressModule as kp

motor = Motor(2,3,4,17,22,27)

kp.init()

def main():
    if kp.getKey('w'):
        motor.move(0.6,0,0.1)
        print('Frente')
    if kp.getKey('s'):
        motor.move(-0.6,0,0.1)
        print('tras')
    if kp.getKey('d'):
        motor.move(0.5,0.3,0.1)
        print('direita')
    if kp.getKey('a'):
        motor.move(0.5,-0.3,0.1)
        print('esqeurda')
    else:
        motor.stop(0.1)

if __name__ == '__main__':
    while True:
        main()