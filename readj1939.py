import cantools
import can
from pprint import pprint
db = cantools.database.load_file('j1939bus_181017_090023.dbc')
bus = can.interface.Bus('vcan0', bustype='socketcan')
canBR = can.BufferedReader()
can.Notifier(bus, [canBR])

while True:
    message = canBR.get_message(timeout=.1)
    db.decode_message(message.arbitration_id, message.data)
