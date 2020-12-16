from time import sleep
class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']
    def running(self):
        while True:
            print(f'Светофор светит {TrafficLight.__color[0]}')
            sleep(7)
            print(f'Светофор светит {TrafficLight.__color[1]}')
            sleep(2)
            print(f'Светофор светит {TrafficLight.__color[2]}')
            sleep(7)
TrafficLight = TrafficLight()
TrafficLight.running()