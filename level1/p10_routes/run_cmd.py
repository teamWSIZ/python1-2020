import subprocess
# output = subprocess.check_output('traceroute 8.8.8.8', shell=True).decode('UTF-8')


# tu na windows można użyć innych ciekawych komend, np. 'net localgroup', lub 'net user'
output = subprocess.check_output('ls -la', shell=True).decode('UTF-8')
print(output.splitlines())

