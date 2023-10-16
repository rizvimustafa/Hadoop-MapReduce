import json
import pandas as pd
import sys

file_path = sys.argv[1]
useful_votes = sys.argv[2]

data_file = open(file_path, errors='ignore')
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)

count = 0

text_file = open('Q3.out.txt', 'w')

for i in data:
    if i['useful'] >= int(useful_votes):
        temp = i['friends'].split(",")
        for friend in temp:
            if i['user_id'] == temp and i['useful'] > int(useful_votes):
                text_file.write(str(i['user_id']) + ' ' + str(friend))

text_file.close()
data_file.close()


