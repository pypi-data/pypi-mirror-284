A class-based interface to the Galileo Flow Sensor
https://microfluidics-innovation-center.com/instruments/wide-range-microfluidic-flow-sensor-with-clogging-detection/


Example 1. Reading a flow rate

First, insert the cartridge to the Base and power on the sensor using type-C USB connector. Make sure that all three flgas on the screen is green.

Next, check the COMPORT number of the sensor. In Windows, you can open the Device Manager and find the COMPORT under Com Ports:


Finally,

you can write the following line to read the flow rate:

'''
import 
galileo_sensor = GalileoFlowSDK("COM18")

while(1):
    time.sleep(1)
    print('flow is ' , galileo_sensor.read_flow())
'''
