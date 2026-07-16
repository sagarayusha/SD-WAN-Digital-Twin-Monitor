import os
import time

# Tumhare routers ke IP addresses yahan likho
routers = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

def check_network():
    print("--- Network Status ---")
    for ip in routers:
        # OS ka ping command chalao
        response = os.system(f"ping -n 1 {ip} > nul")
        if response == 0:
            print(f"Router {ip} is UP")
        else:
            print(f"Router {ip} is DOWN")

# Har 5 second mein status check karo
while True:
    check_network()
    time.sleep(5)