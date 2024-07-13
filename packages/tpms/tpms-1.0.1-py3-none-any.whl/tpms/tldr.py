from tpms import TPMS
import time

tpms_system = TPMS(
    # port="/dev/ttyUSB0",  # Adjust this to the correct serial port
    baudrate=19200,  # Set baud rate according to your device specifications
    temp_unit="Fahrenheit",  # Convert temperature readings to Fahrenheit
    pressure_unit="psi",  # Convert pressure readings to psi
    debug=False,  # Enable debug mode for detailed logging
)

data = tpms_system.oneshot()

for tyre, info in data.items():
    print(tyre, info)
