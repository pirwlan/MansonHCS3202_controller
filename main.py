""" Script to control on/off switching of Manson HC3602 Power Supply."""

import serial, time


# Initializing usb connection to Manson power supply
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0,
			bytesize=serial.EIGHTBITS,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE)


def initialize(voltage_settings = "VOLT155\r", current_settings = "CURR020\r"):
    """Initializes connection to Manson Powere Supply. Sets voltage and current.
       Defaults are 15.5 Volt and 0.20 Ampere.
       :param voltage_settings: Voltage value
       :param current_settings: Ampere value"""

    z = 1

    while z:

        ser.write(voltage_settings)
        time.sleep(0.5)
        response=ser.readline()

        if response == '':
            continue


    while z:

        ser.write(current_settings)
        time.sleep(0.5)
        response=ser.readline()

        if response == '':
            continue


def single_illumination(time_light_on = 5, time_light_off  = 25):
    """ One round of illumination, with 5 secondes light on and 25 seconds ligth off.
        :param time_light_on: Switches power on for 5 seconds (default).
        :param time_light_off: Switches power off for 25 seconds (default)."""

    w = 1

    while w:

        ser.write("SOUT0\r")
        time.sleep(0.5)
        response=ser.readline()

        if response == '':
            continue


    time.sleep(time_light_on)

    while w:

        ser.write("SOUT1\r")
        time.sleep(0.5)
        response=ser.readline()

        if response == '':
            continue

    time.sleep(time_light_off)


def illuminate(time_in_minutes,
               voltage_settings="VOLT155\r",
               current_settings = "CURR020\r",
               time_light_on=5,
               time_light_off=25
               ):
    """
    starts illumination for given times in minutes.
    :param time_in_minutes:
    :param voltage_settings:
    :param current_settings:
    :param time_light_on:
    :param time_light_off:
    """
    
    initialize(voltage_settings, current_settings)
    start_time = time.time()
    end_time = start_time + time_in_minutes * 60

    while time.time() < end_time:
        single_illumination(time_light_on, time_light_off)


if ser.isOpen():

    x = 1

    try:

        ser.flushInput()
        ser.flushOutput()

        initialize(voltage_settings="VOLT130\r")

        while x:

            initialize()
            
            illuminate(30)

            time.sleep(3600)
