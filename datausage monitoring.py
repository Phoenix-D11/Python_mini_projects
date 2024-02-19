import time
import psutil
import pandas as pd
import threading

# Initialize DataFrame
df = pd.DataFrame(columns=['time', 'bytes_sent', 'bytes_recv'])

# Function to get network details
def get_network_details():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

# Flag to control the monitoring thread
stop_thread = False

# Monitoring function to be run in a separate thread
def monitor():
    while True:
        if stop_thread:
            break
        bytes_sent, bytes_recv = get_network_details()
        df.loc[pd.Timestamp.now()] = [pd.Timestamp.now(), bytes_sent, bytes_recv]
        time.sleep(1)

# Start monitoring
while True:
    user_input = input("Enter 'start' to start monitoring, 'stop' to stop: ")
    if user_input.lower() == 'start':
        stop_thread = False
        t = threading.Thread(target=monitor)
        t.start()
    elif user_input.lower() == 'stop':
        stop_thread = True
        t.join()  # Wait for the monitoring thread to finish
        print(df)
        break
    else:
        print("Invalid input. Please enter 'start' or 'stop'.")
