import gpiozero
from gpiozero import DigitalOutputDevice
import time

class Solenoid(DigitalOutputDevice):
    def __init__(self, guid):
        super().__init__(guid)
    def timedon(self, t):
        self.on()
        time.sleep(t)
        self.off()


pump = DigitalOutputDevice(26)
waterSolenoid = Solenoid(27)
nutrientSolenoid = Solenoid(17)
levelOneSolenoid = Solenoid(22)
levelTwoSolenoid = Solenoid(10)
levelThreeSolenoid = Solenoid(9)
levelFourSolenoid = Solenoid(11)
levelFiveSolenoid = Solenoid(0)
transferSolenoid = Solenoid()


def waterCycle(solenoids, cycleTime):
    
    #check tank levels
    #need to add a constant check for tank level 
    #if it hits empty stop cycle
    pump.on()
    time.sleep(1)
    waterSolenoid.on()
    time.sleep(1)
    for i in solenoids:
        i.on()
        time.sleep(cycleTime)
        i.off()
    time.sleep(1)
    waterSolenoid.off()
    time.sleep(1)
    pump.off()

    #check tank levels

    #check tank levels

def nutrientCycle(solenoids, cycleTime):
    
    #check tank levels

    pump.on()
    time.sleep(1)
    nutrientSolenoid.on()
    time.sleep(1)
    for i in solenoids:
        i.on()
        time.sleep(cycleTime)
        i.off()
    time.sleep(1)
    nutrientSolenoid.off()
    time.sleep(1)
    pump.off()

def tankTransfer():
    #check tank levels
    transferSolenoid.on()
    #need to figure out how long valve shoudl stay open for transfer
    time.sleep(XXX)
    transferSolenoid.off()
    #check tank levels
        

levels = [levelOneSolenoid,levelTwoSolenoid,levelThreeSolenoid,levelFourSolenoid,levelFiveSolenoid]
waterCycle(levels, 2)
nutrientCycle(levels, 2)




