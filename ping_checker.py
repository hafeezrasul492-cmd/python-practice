import subprocess

sites = ["google.com.", "youtube.com.", "github.com.", "fakesite12345.com."]

for site in sites:
    result = subprocess.run(["ping", "-c", "2", "-W", "2", site], capture_output=True)
    if result.returncode == 0:
        print(site, "Is Up")
    else:
        print(site, "Is Down")

