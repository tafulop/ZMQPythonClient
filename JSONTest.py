import json

message = json.dumps({'JOINT_ID': 'J1', 'MESSAGE_TYPE': 'JOINT_DATA_REQ'}, indent=4, separators=(',', ': '))

print message