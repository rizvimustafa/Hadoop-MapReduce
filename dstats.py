import json
import pandas as pd
import sys

file_path = sys.argv[1]
City = sys.argv[2]
State = sys.argv[3]

data_file = open(file_path, errors='ignore')
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)

number_of_businesses = 0
avg_stars_businesses = 0
number_of_restaurants = 0
avg_stars_restaurants = 0
avg_reviews_businesses = 0
avg_reviews_restaurants = 0

sum1 = 0.0
sum2 = 0.0
count1 = 0
count2 = 0

for i in data:
    if i['city'] == City and i['state'] == State:
        number_of_businesses = number_of_businesses + 1
        sum1 = sum1 + (i['stars'])
        count1 = count1 + int(i['review_count'])
        if 'Restaurants' in str(i['categories']):
            number_of_restaurants = number_of_restaurants + 1
            sum2 = sum2 + i['stars']
            count2 = count2 + int(i['review_count'])

avg_stars_businesses = sum1 / number_of_businesses
avg_stars_restaurants = sum2 / number_of_restaurants
avg_reviews_businesses = count1 / number_of_businesses
avg_reviews_restaurants = count2 / number_of_restaurants

text_file = open('Q1.out.txt', 'w')
text_file.write(str(number_of_businesses) + '\n')
text_file.write(str(round(avg_stars_businesses, 2)) + '\n')
text_file.write(str(number_of_restaurants) + '\n')
text_file.write(str(round(avg_stars_restaurants, 2)) + '\n')
text_file.write(str(round(avg_reviews_businesses, 2)) + '\n')
text_file.write(str(round(avg_reviews_restaurants, 2)) + '\n')
text_file.close()

data_file.close()
