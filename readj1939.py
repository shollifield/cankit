import cantools
import can
from pprint import pprint
db = cantools.database.load_file('j1939_20121116_TSC1_PTO_canalyser_11.dbc')
bus = can.interface.Bus('can0', bustype='socketcan')
message = bus.recv()
db.decode_message(message.arbitration_id, message.data)
