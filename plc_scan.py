import logging
import sys
import json

import numpy as np

# pip install cpppo
from cip import CIP, CIP_Path
import plc
from config import *
from cpppo.server.enip import client
from cpppo.server.enip.get_attribute import attribute_operations

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.ERROR)


def save_result(success_class_info_list):

    with open(OUTPUT_FILE_NAME, "w") as fp:
        json.dump(success_class_info_list, fp)


def scan_one(class_name, instance_id, attribute_id = None):
    
    success_service = set()
    class_id = CLASS_CODES[class_name]

    for service_id in CLASS_SERVICE_MAP[class_name]:
        plc_client = plc.PLCClient(PLC_HOST)

        if not plc_client.connected:
            logging.error(("Cannot connect to server"))
            sys.exit(1)
      
        # Make packet detail                  
        cippkt = CIP(service = service_id, 
                     path = CIP_Path.make(class_id     = class_id, 
                                          instance_id  = instance_id, 
                                          attribute_id = attribute_id)
                    )

        # Send a CIP request
        plc_client.send_rr_cip(cippkt)

        # Receive the response
        resppkt = plc_client.recv_enippkt()

        #resppkt.show()

        try:
            enip_tcp_status = resppkt["ENIP_TCP"].status
            cip_tcp_status  = resppkt["CIP_ResponseStatus"].status                
        except:
            cip_tcp_status = None            

        if enip_tcp_status == 0x0 and cip_tcp_status == 0x0:  # SUCCESS
            success_service.add(service_id)
            

    logging.debug(("Class "+ str(class_name) + " supports serives " + str(success_service)))

    return success_service


def scan_message_router(tag_name, position, values, types):
    success_service = set()

    # Read Tag 0x4c
    read_tag = [tag_name + '[' + str(position) + ']']

    with client.connector(host=PLC_HOST) as conn:        
        for index, descr, op, reply, status, value in conn.pipeline(
            operations=client.parse_operations(read_tag), depth=2):
            pass
            
        if status == 0x00:
            success_service.add(0x4c)
    
    # Write Tag 0x4d
    write_tag = [str(tag_name + '[' + str(position) + ']=' + "(" + types + ")" + str(values))]   
    
    with client.connector(host=PLC_HOST) as conn:
        for index, descr, op, reply, status, value in conn.pipeline(
            operations=client.parse_operations(write_tag), depth=2):
            pass

        if status == 0x00:
            success_service.add(0x4d)
    
    print(("Class Message Router 0x02 supports specifics serives " + str(success_service)))

    return success_service


def scan_all():
    success_class_info_list = []
    success_class_service_list = {}

    # initailize success_class_service
    for class_name in CLASS_CODES.keys():
        success_class_service_list[class_name] = set()    
 
    for class_name in CLASS_CODES.keys():
        class_id = CLASS_CODES[class_name]
        
        for instance_id in range(INSTANCE_ID_RANGE[0], INSTANCE_ID_RANGE[1]):

            for attribute_id in range(ATTRIBUTE_RANGE[0], ATTRIBUTE_RANGE[1]):

                success_service = scan_one(class_name, instance_id, attribute_id)                
                success_class_service_list[class_name].update(success_service)

                for service_id in success_service:
                    class_info = { 
                                   "class_name"  : class_name,
                                   "class_id"    : hex(class_id),                
                                   "instance_id" : instance_id,
                                   "attribute_id": attribute_id,
                                   "service_id"  : hex(service_id),
                                 }

                    success_class_info_list.append(class_info)



    for class_name in CLASS_CODES.keys():
        if len(success_class_service_list[class_name]) > 0:
            print(("Class " + str(class_name) + " " + str(CLASS_CODES[class_name]) + " supports serives " + str(success_class_service_list[class_name])))   


    return success_class_info_list


def main():
    """
    class_name  = "Identity"
    instance_id = 1
    scan_one(class_name, instance_id)
    """

    """
    success_class_info_list = scan_all()
    save_result(success_class_info_list)
    """

    scan_message_router(tag_name="TEXT", position=0, values="Hello", types="SSTRING")

    
if __name__ == "__main__":
    main()
   