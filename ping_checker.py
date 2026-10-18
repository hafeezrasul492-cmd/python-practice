import subprocess
from datetime import datetime

def check_site(site):
    result = subprocess.run(["ping", "-c", "2", "-W", "2", site], capture_output=True)
    return result.returncode == 0

sites = ["google.com.", "youtube.com.", "github.com.", "fakesite12345.com."]

with open("ping_log.txt", "a") as f:
    for site in sites:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if check_site(site):
            line = time + " " + site + " UP"
        else:
            line = time + " " + site + " DOWN"
        print(line)
        f.write(line + "\n")
