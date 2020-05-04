import os
import subprocess
from datetime import datetime
from time import sleep
# os.system('tracert 192.207.0.1')
while True:

    with open('ah.txt', 'a') as f:
        
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        f.write(f"{current_time} \n")
        
        process = subprocess.Popen(['tracert', '192.207.0.1'], stdout=f)

        sleep(1800)
