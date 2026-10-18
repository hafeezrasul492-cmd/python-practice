import subprocess

def check_site(site):
    result = subprocess.run(["ping", "-c", "2", "-W", "2", site], capture_output=True)
    return result.returncode == 0

print(check_site("google.com."))
print(check_site("fakesite12345.com."))
