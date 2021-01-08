import logging
import sys

from cip import CIP, CIP_Path
import plc
import json


from config import *


success_list=[]
success_service_list=[]


for service_name in SERVICE_CODES.keys():
    service_id=SERVICE_CODES[service_name]

    for class_name in CLASS_CODES.keys():
        class_id=CLASS_CODES[class_name]
        
        for instance_id in range(INSTANCE_ID_RANGE[0],INSTANCE_ID_RANGE[1]):

            logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)

            # Connect to PLC
            client = plc.PLCClient(PLC_HOST)
            if not client.connected:
                sys.exit(1)
            print("Established session {}".format(client.session_id))

            # Send a CIP ReadTag request
            cippkt = CIP(service=service_id, path=CIP_Path.make(class_id=int(class_id), instance_id=instance_id))
            client.send_rr_cip(cippkt)

            # Receive the response and show it
            resppkt = client.recv_enippkt()

            enip_tcp_status=resppkt["ENIP_TCP"].status
            service_info={"name":service_name+class_name+str(instance_id),"service_name":service_name,"class_name":class_name,"service_id":service_id,"class_id":class_id,"instance_id":instance_id}

            if enip_tcp_status==0:
                success_list.append(service_info)
                success_service_list.append(service_name)
                print("[success]"+str(service_info))

                
            else:
                print("[fail]"+str(service_info))


print("num of success:"+str(len(success_list)))
print("num of success service:"+str(len(list(set(success_service_list)))))


with open(OUTPUT_FILE_NAME,"w") as fp:
    json.dump(success_list, fp)





