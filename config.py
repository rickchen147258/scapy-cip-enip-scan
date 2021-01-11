PLC_HOST = "192.168.1.189"

OUTPUT_FILE_NAME = "sucess_list.json"

INSTANCE_ID_RANGE = (0, 5)
ATTRIBUTE_RANGE   = (1, 5)

CLASS_CODES = {
	"Identity"                              : 0x01, 
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
	"Quality of Service Object"             : 0x48,
	"ControlNet Object"                     : 0xF0,
	"ControlNet Keeper Object"              : 0xF1,
	"ControlNet Scheduling Object"          : 0xF2,
	"Connection Configuration Object"       : 0xF3,
	"Port Object"                           : 0xF4,
	"TCP/IP Interface Object"               : 0xF5,
	"EtherNet Link Object"                  : 0xF6,
}


SERVICE_CODES = {
	# 0x00 - 0x31 CIP COMMON SERVICE CODE
    "Get_Attribute_All"             : 0x01,
    "Set_Attribute_All"             : 0x02,
    "Get_Attribute_List"            : 0x03,
    "Set_Attribute_List"            : 0x04,
    "Reset"                         : 0x05,
    "Start"                         : 0x06,
    "Stop"                          : 0x07,
    "Create"                        : 0x08,
    "Delete"                        : 0x09,
    "Multiple_Service_Packet"       : 0x0a,
    "Apply_attributes"              : 0x0d,
    "Get_Attribute_Single"          : 0x0e,
    "Set_Attribute_Single"          : 0x10,
    "Find_Next_Object_Instance"     : 0x11,    
    "Get_Member"                    : 0x18,
    "Set_Member"                    : 0x19,
    "Insert_Member"                 : 0x1A,
    "Remove_Member"                 : 0x1B,
    # 0x4B - 0x63 CLASS SPECIFICS SERVICE CODE (same code in different class has different meanings)
    "Execute_PCCC_Service"          : 0x4B,  # PCCC = Programmable Controller Communication Commands
    "Read_Tag_Service"              : 0x4C,
    "Write_Tag_Service"             : 0x4D,
    "Read_Modify_Write_Tag_Service" : 0x4E,
    "Read_Other_Tag_Service"        : 0x4F,  
    "Read_Tag_Fragmented_Service"   : 0x52,
    "Write_Tag_Fragmented_Service"  : 0x53,
    "Forward_Open"                  : 0x54,
}

CLASS_SERVICE_MAP = {
	"Identity"                              : [0x01, 0x05, 0x0E, 0x10, 0x11], # CIP Common Specification Page 5-11
	"Message Router"                        : [0x01, 0x0E], # CIP Common Specification Page 5-17
	"DeviceNet"                             : [],
	"Assembly"                              : [0x01, 0x08, 0x09, 0x0E, 0x10, 0x18, 0x19, 0x1A, 0x1B], # CIP Common Specification Page 5-22
	"Connection"                            : [0x01, 0x05, 0x08, 0x09, 0x0E, 0x11], # CIP Common Specification Page 3-9
	"Connection Manage"                     : [0x01, 0x0E], # CIP Common Specification Page 3-53
	"Register"                              : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-31
	"Discrete Input Point"                  : [0x01, 0x02, 0x0E, 0x10], # CIP Common Specification Page 5-31
	"Discrete Output Point"                 : [0x01, 0x02, 0x0E, 0x10], # CIP Common Specification Page 5-33
	"Analog Input Point"                    : [0x01, 0x02, 0x0E, 0x10], # CIP Common Specification Page 5-49
	"Analog Output Point"                   : [0x01, 0x02, 0x0E, 0x10], # CIP Common Specification Page 5-58
	"Presence Sensing"                      : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-69
	"Parameter"                             : [0x01, 0x05, 0x0E, 0x10, 0x15, 0x16], # CIP Common Specification Page 5-77
	"Parameter Group"                       : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-84
	"Group"                                 : [0x01, 0x0E], # CIP Common Specification Page 5-88
	"Discrete Input Group"                  : [0x01, 0x02, 0x0E, 0x10], # CIP Common Specification Page 5-93
	"Discrete Output Group"                 : [0x01, 0x02, 0x0E, 0x10], # CIP Common Specification Page 5-99
	"Discrete Group"                        : [0x01, 0x0E], # CIP Common Specification Page 5-104
	"Analog Input Group"                    : [0x01, 0x02, 0x10, 0x0E], # CIP Common Specification Page 5-108
	"Analog Output Group"                   : [0x01, 0x02, 0x10, 0x0E], # CIP Common Specification Page 5-113
	"Analog Group"                          : [0x01, 0x10, 0x0E], # CIP Common Specification Page 5-119
	"Position Sensor Object"                : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-124
	"Position Controller Supervisor Object" : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-133
	"Position Controller Object"            : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-142
	"Block Sequencer Object"                : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-147
	"Command Block Object"                  : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-153
	"Motor Data Object"                     : [0x01, 0x0E, 0x10, 0x15, 0x16], # CIP Common Specification Page 5-156
	"Control Supervisor Object"             : [0x01, 0x05, 0x0E, 0x10], # CIP Common Specification Page 5-161
	"AC/DC Drive Object"                    : [0x01, 0x0E, 0x10, 0x15, 0x16], # CIP Common Specification Page 5-170
	"Acknowledge Handler Object"            : [0x01, 0x08, 0x09, 0x0E], # CIP Common Specification Page 5-176
	"Overload Object"                       : [0x01, 0x0E, 0x10, 0x15, 0x16], # CIP Common Specification Page 5-187
	"Softstart Object"                      : [0x01, 0x0E, 0x10, 0x15, 0x16], # CIP Common Specification Page 5-190
	"Selection Object"                      : [0x01, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0E], # CIP Common Specification Page 5-195
	"S-Device Supervisor Object"            : [0x01, 0x05, 0x06, 0x07, 0x0E, 0x10], # CIP Common Specification Page 5-214
	"S-Analog Sensor Object"                : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-227
	"S-Analog Actuator Object"              : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-254
	"S-Single Stage Controller Object"      : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-261
	"S-Gas Calibration Object"              : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-267
	"Trip Point Object"                     : [0x01, 0x0E, 0x10], # CIP Common Specification Page 5-273
	"Quality of Service Object"             : [0x01, 0x0E], # From OpENer
	"ControlNet Object"                     : [],
	"ControlNet Keeper Object"              : [],
	"ControlNet Scheduling Object"          : [],
	"Connection Configuration Object"       : [0x01, 0x02, 0x08, 0x09, 0x0E, 0x10, 0x15],
	"Port Object"                           : [0x01, 0x0E], # EtherNet/IP Specification, Volume 1 Page 3-89
	"TCP/IP Interface Object"               : [0x01, 0x02, 0x0E, 0x10], # EtherNet/IP Specification, Volume 2 Page 5-4
	"EtherNet Link Object"                  : [0x01, 0x0E, 0x10], # EtherNet/IP Specification, Volume 2 Page 5-15
}

CLASS_SPECIFICS_SERVICE_MAP = {
	"Message Router"                        : [0x4C, 0x4D],
	"Connection Manage"                     : [0x4E, 0x54, 0x5A, 0x5B],
}