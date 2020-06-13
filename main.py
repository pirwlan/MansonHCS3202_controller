""" Script to control on/off switching of Manson HC3602 Power Supply."""

import datetime
import serial
import time


def logging(log_message: str):
    """
    Simple logging in log.txt
    Args:
        log_message: str - Message, that will be appended to the log.txt
    """

    log_file = 'log.txt'
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a+') as log:
        log.write(f'{current_date} - {log_message} \n')


def initialize(voltage_settings: str = "VOLT155\r", current_settings: str = "CURR020\r"):
    """
    Initializes connection to Manson Powere Supply.
    Sets voltage and current for upcoming illumination.

    Args:
        voltage_settings: string - Voltage value (three digits: 10.0V := VOLT100\r).
                                    Default "VOLT155\r" := 15.5 V
        current_settings: string - Ampere value (three digits: 1 Amp := CURR100\r)
                                    Default "0.20 Ampere" := 0.2 Amp
    """

    z = 1

    while z:

        ser.write(voltage_settings)
        time.sleep(0.5)
        response = ser.readline()

        if response == '':
            continue

    while z:

        ser.write(current_settings)
        time.sleep(0.5)
        response = ser.readline()

        if response == '':
            continue


def single_illumination(illumination_on: int = 5, illumination_off: int  = 25):
    """
    One single round of illumination.

    Args:
        illumination_on: integer - switches illumination on for X seconds. Default: 5 seconds.
        illumination_off: integer - switches illumination off for X seconds. Default: 25 seconds.
    """

    w = 1

    while w:

        ser.write("SOUT0\r")
        time.sleep(0.5)
        response = ser.readline()

        if response == '':
            continue

    time.sleep(illumination_on)

    while w:

        ser.write("SOUT1\r")
        time.sleep(0.5)
        response = ser.readline()

        if response == '':
            continue

    time.sleep(illumination_off)


def illuminate(illumination_time: int,
               voltage_settings: str = "VOLT155\r",
               current_settings: str = "CURR020\r",
               individual_illumination_on: int = 5,
               individual_illumination_off: int= 25
               ):
    """
    starts illumination for given times in minutes.

    Args:
        illumination_time: integer - Total time of illumination block in Minutes.
        voltage_settings: string - Voltage value (three digits: 10.0V := VOLT100\r).
                                    Default VOLT155\r := 15.5V
        current_settings: string - Ampere value (three digits: 1 Amp := CURR100\r)
                                    Default CURR020\r := 0.2 Amp
        individual_illumination_on: int - switches illumination on for X seconds. Default: 5 seconds.
        individual_illumination_off: int - switches illumination off for X seconds. Default: 25 seconds.
    """
    
    initialize(voltage_settings, current_settings)
    start_time = time.time()
    end_time = start_time + illumination_time * 60

    while time.time() < end_time:
        single_illumination(individual_illumination_on, individual_illumination_off)


def start_illumination():

    # Initializing usb connection to Manson power supply

    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE)

    except serial.serialutil.SerialException:
        logging('Connection to USB device could not be established!.')

    if ser.isOpen():

        x = 1

        try:

            ser.flushInput()
            ser.flushOutput()

            initialize(voltage_settings="VOLT130\r")
            logging('Experiment started.')
            while x:
                logging('Illumination cirle successfully started.')
                # illumination for 1 hour, 13V, 0.2Amp and 5s/20s cycles
                illuminate(illumination_time=60,
                           voltage_settings="VOLT130\r",
                           current_settings="CURR020\r",
                           individual_illumination_on=5,
                           individual_illumination_off=20)

                # illumination off for 1 hour
                time.sleep(3600)
                logging('Illumination circle successfully finised.')

        except:
            logging('Error occured, connetion interrupted.')


if __name__ == '__main__':
    start_illumination()