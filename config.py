PLC_HOST="127.0.0.1"

OUTPUT_FILE_NAME="sucess_list.json"

INSTANCE_ID_RANGE=(0,5)



CLASS_CODES = {
	"Identity"                              : 0x01, # Page 5-6
	"Message Router"                        : 0x02,
	"DeviceNet"                             : 0x03,
	"Assembly"                              : 0x04,
	"Connection"                            : 0x05,
	"Connection Manage"                     : 0x06,
	"Register"                              : 0x07,
	"Discrete Input Point"                  : 0x08,
	"Discrete Output Point"                 : 0x09,
	"Analog Input Point"                    : 0x0A,
	"Analog Output Point"                   : 0x0B,
	"Presence Sensing"                      : 0x0E,
	"Parameter"                             : 0x0F,
	"Parameter Group"                       : 0x10,
	"Group"                                 : 0x12,
	"Discrete Input Group"                  : 0x1D,
	"Discrete Output Group"                 : 0x1E,
	"Discrete Group"                        : 0x1F,
	"Analog Input Group"                    : 0x20,
	"Analog Output Group"                   : 0x21,
	"Analog Group"                          : 0x22,
	"Position Sensor Object"                : 0x23,
	"Position Controller Supervisor Object" : 0x24,
	"Position Controller Object"            : 0x25,
	"Block Sequencer Object"                : 0x26,
	"Command Block Object"                  : 0x27,
	"Motor Data Object"                     : 0x28,
	"Control Supervisor Object"             : 0x29,
	"AC/DC Drive Object"                    : 0x2A,
	"Acknowledge Handler Object"            : 0x2B,
	"Overload Object"                       : 0x2C,
	"Softstart Object"                      : 0x2D,
	"Selection Object"                      : 0x2E,
	"S-Device Supervisor Object"            : 0x30,
	"S-Analog Sensor Object"                : 0x31,
	"S-Analog Actuator Object"              : 0x32,
	"S-Single Stage Controller Object"      : 0x33,
	"S-Gas Calibration Object"              : 0x34,
	"Trip Point Object"                     : 0x35,
	"ControlNet Object"                     : 0xF0,
	"ControlNet Keeper Object"              : 0xF1,
	"ControlNet Scheduling Object"          : 0xF2,
	"Connection Configuration Object"       : 0xF3,
	"Port Object"                           : 0xF4,
	"TCP/IP Interface Object"               : 0xF5,
	"EtherNet Link Object"                  : 0xF6
}



SERVICE_CODES = {
        "Get_Attribute_All": 0x01,
        "Set_Attribute_All": 0x02,
        "Get_Attribute_List": 0x03,
        "Set_Attribute_List": 0x04,
        "Reset": 0x05,
        "Start": 0x06,
        "Stop": 0x07,
        "Create": 0x08,
        "Delete": 0x09,
        "Multiple_Service_Packet": 0x0a,
        "Apply_attributes": 0x0d,
        "Get_Attribute_Single": 0x0e,
        "Set_Attribute_Single": 0x10,
        "Execute_PCCC_Service": 0x4b,  # PCCC = Programmable Controller Communication Commands
        "Read_Tag_Service": 0x4c,
        "Write_Tag_Service": 0x4d,
        "Read_Modify_Write_Tag_Service": 0x4e,
        "Read_Other_Tag_Service": 0x4f,  
        "Read_Tag_Fragmented_Service": 0x52,
        "Write_Tag_Fragmented_Service": 0x53,
        "Forward_Open?": 0x54,
}
