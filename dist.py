import json
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

file_path = sys.argv[1]
City = sys.argv[2]
State = sys.argv[3]

data_file = open(file_path, errors='ignore')
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)

American_traditional = 0
Thai = 0
Mediterranean = 0
Greek = 0
American_new = 0
Indian = 0
Mexican = 0
Taiwanese = 0
Vietnamese = 0
Brazilian = 0
Cuban = 0
Caribbean = 0
German = 0
Asian_fusion = 0
Chinese = 0
Latin_american = 0
Middle_eastern = 0
Italian = 0
Southern = 0
Japanese = 0
Turkish = 0
Hawaiian = 0
Lebanese = 0
French = 0
Filipino = 0
Canadian_new = 0

cuisines = []

sum1 = 0.0
sum2 = 0.0
count1 = 0
count2 = 0

for i in data:
    if i['city'] == City and i['state'] == State:
        if 'Restaurants' and 'American (Traditional)' in str(i['categories']):
            American_traditional = American_traditional + 1
        if 'Restaurants' and 'Thai' in str(i['categories']):
            Thai = Thai + 1
        if 'Restaurants' and 'Mediterranean' in str(i['categories']):
            Mediterranean = Mediterranean + 1
        if 'Restaurants' and 'Greek' in str(i['categories']):
            Greek = Greek + 1
        if 'Restaurants' and 'American (New)' in str(i['categories']):
            American_new = American_new + 1
        if 'Restaurants' and 'Indian' in str(i['categories']):
            Indian = Indian + 1
        if 'Restaurants' and 'Mexican' in str(i['categories']):
            Mexican = Mexican + 1
        if 'Restaurants' and 'Taiwanese' in str(i['categories']):
            Taiwanese = Taiwanese + 1
        if 'Restaurants' and 'Vietnamese' in str(i['categories']):
            Vietnamese = Vietnamese + 1
        if 'Restaurants' and 'Brazilian' in str(i['categories']):
            Brazilian = Brazilian + 1
        if 'Restaurants' and 'Cuban' in str(i['categories']):
            Cuban = Cuban + 1
        if 'Restaurants' and 'Caribbean' in str(i['categories']):
            Caribbean = Caribbean + 1
        if 'Restaurants' and 'German' in str(i['categories']):
            German = German + 1
        if 'Restaurants' and 'Asian Fusion' in str(i['categories']):
            Asian_fusion = Asian_fusion + 1
        if 'Restaurants' and 'Chinese' in str(i['categories']):
            Chinese = Chinese + 1
        if 'Restaurants' and 'Latin American' in str(i['categories']):
            Latin_american = Latin_american + 1
        if 'Restaurants' and 'Middle Eastern' in str(i['categories']):
            Middle_eastern = Middle_eastern + 1
        if 'Restaurants' and 'Italian' in str(i['categories']):
            Italian = Italian + 1
        if 'Restaurants' and 'Southern' in str(i['categories']):
            Southern = Southern + 1
        if 'Restaurants' and 'Japanese' in str(i['categories']):
            Japanese = Japanese + 1
        if 'Restaurants' and 'Turkish' in str(i['categories']):
            Turkish = Turkish + 1
        if 'Restaurants' and 'Hawaiian' in str(i['categories']):
            Hawaiian = Hawaiian + 1
        if 'Restaurants' and 'Lebanese' in str(i['categories']):
            Lebanese = Lebanese + 1
        if 'Restaurants' and 'French' in str(i['categories']):
            French = French + 1
        if 'Restaurants' and 'Filipino' in str(i['categories']):
            Filipino = Filipino + 1
        if 'Restaurants' and 'Canadian (New)' in str(i['categories']):
            Canadian_new = Canadian_new + 1

AT = "American (Traditional):" + str(American_traditional)
thai = "Thai:" + str(Thai)
mediterranean = "Mediterranean:" + str(Mediterranean)
greek = "Greek:" + str(Greek)
AN = "American (New):" + str(American_new)
indian = "Indian:" + str(Indian)
mexican = "Mexican:" + str(Mexican)
taiwanese = "Taiwanese:" + str(Taiwanese)
vietnamese = "Vietnamese:" + str(Vietnamese)
brazilian = "Brazilian:" + str(Brazilian)
cuban = "Cuban:" + str(Cuban)
caribbean = "Caribbean:" + str(Caribbean)
german = "German:" + str(German)
asian_fusion = "Asian Fusion:" + str(Asian_fusion)
chinese = "Chinese:" + str(Chinese)
latin_american = "Latin American:" + str(Latin_american)
middle_eastern = "Middle Eastern:" + str(Middle_eastern)
italian = "Italian:" + str(Italian)
southern = "Southern:" + str(Southern)
japanese = "Japanese:" + str(Japanese)
turkish = "Turkish:" + str(Turkish)
hawaiian = "Hawaiian:" + str(Hawaiian)
lebanese = "Lebanese:" + str(Lebanese)
french = "French:" + str(French)
filipino = "Filipino:" + str(Filipino)
canadian_new = "Canadian (New):" + str(Canadian_new)

cuisines = [AT, thai, mediterranean, greek, AN, indian, mexican, taiwanese, vietnamese, brazilian, cuban, caribbean,
            german, asian_fusion, chinese, latin_american, middle_eastern, italian, southern, japanese, turkish,
            hawaiian, lebanese, french, filipino, canadian_new]


def extract_number(string):
    return int(string.split(':')[1])


def extract_string(string):
    return string.split(':')[0]


cuisines.sort(key=extract_number)

cuisines.reverse()

cuisines_y = []
cuisines_x = []

for cuisine in cuisines[:5]:
    cuisines_y.append(extract_number(cuisine))
    cuisines_x.append(extract_string(cuisine))

text_file = open('Q2_part1.out.txt', 'w')
for cuisine in cuisines[:10]:
    text_file.write(cuisine + '\n')
text_file.close()

American_traditional_r = 0
American_traditional_c = 0
Thai_r = 0
Thai_c = 0
Mediterranean_r = 0
Mediterranean_c = 0
Greek_r = 0
Greek_c = 0
American_new_r = 0
American_new_c = 0
Indian_r = 0
Indian_c = 0
Mexican_r = 0
Mexican_c = 0
Taiwanese_r = 0
Taiwanese_c = 0
Vietnamese_r = 0
Vietnamese_c = 0
Brazilian_r = 0
Brazilian_c = 0
Cuban_r = 0
Cuban_c = 0
Caribbean_r = 0
Caribbean_c = 0
German_r = 0
German_c = 0
Asian_fusion_r = 0
Asian_fusion_c = 0
Chinese_r = 0
Chinese_c = 0
Latin_american_r = 0
Latin_american_c = 0
Middle_eastern_r = 0
Middle_eastern_c = 0
Italian_r = 0
Italian_c = 0
Southern_r = 0
Southern_c = 0
Japanese_r = 0
Japanese_c = 0
Turkish_r = 0
Turkish_c = 0
Hawaiian_r = 0
Hawaiian_c = 0
Lebanese_r = 0
Lebanese_c = 0
French_r = 0
French_c = 0
Filipino_r = 0
Filipino_c = 0
Canadian_new_r = 0
Canadian_new_c = 0
for i in data:
    if i['city'] == City and i['state'] == State:
        if 'Restaurants' and 'American (Traditional)' in str(i['categories']):
            American_traditional_r += i['review_count']
            American_traditional_c = American_traditional_c + 1
        if 'Restaurants' and 'Thai' in str(i['categories']):
            Thai_r += i['review_count']
            Thai_c = Thai_c + 1
        if 'Restaurants' and 'Mediterranean' in str(i['categories']):
            Mediterranean_r += i['review_count']
            Mediterranean_c = Mediterranean_c + 1
        if 'Restaurants' and 'Greek' in str(i['categories']):
            Greek_r += i['review_count']
            Greek_c = Greek_c + 1
        if 'Restaurants' and 'American (New)' in str(i['categories']):
            American_new_r += i['review_count']
            American_new_c = American_new_c + 1
        if 'Restaurants' and 'Indian' in str(i['categories']):
            Indian_r += i['review_count']
            Indian_c = Indian_c + 1
        if 'Restaurants' and 'Mexican' in str(i['categories']):
            Mexican_r += i['review_count']
            Mexican_c = Mexican_c + 1
        if 'Restaurants' and 'Taiwanese' in str(i['categories']):
            Taiwanese_r += i['review_count']
            Taiwanese_c = Taiwanese_c + 1
        if 'Restaurants' and 'Vietnamese' in str(i['categories']):
            Vietnamese_r += i['review_count']
            Vietnamese_c = Vietnamese_c + 1
        if 'Restaurants' and 'Brazilian' in str(i['categories']):
            Brazilian_r += i['review_count']
            Brazilian_c = Brazilian_c + 1
        if 'Restaurants' and 'Cuban' in str(i['categories']):
            Cuban_r += i['review_count']
            Cuban_c = Cuban_c + 1
        if 'Restaurants' and 'Caribbean' in str(i['categories']):
            Caribbean_r += i['review_count']
            Caribbean_c = Caribbean_c + 1
        if 'Restaurants' and 'German' in str(i['categories']):
            German_r += i['review_count']
            German_c = German_c + 1
        if 'Restaurants' and 'Asian Fusion' in str(i['categories']):
            Asian_fusion_r += i['review_count']
            Asian_fusion_c = Asian_fusion_c + 1
        if 'Restaurants' and 'Chinese' in str(i['categories']):
            Chinese_r += i['review_count']
            Chinese_c = Chinese_c + 1
        if 'Restaurants' and 'Latin American' in str(i['categories']):
            Latin_american_r += i['review_count']
            Latin_american_c = Latin_american_c + 1
        if 'Restaurants' and 'Middle Eastern' in str(i['categories']):
            Middle_eastern_r += i['review_count']
            Middle_eastern_c = Middle_eastern_c + 1
        if 'Restaurants' and 'Italian' in str(i['categories']):
            Italian_r += i['review_count']
            Italian_c = Italian_c + 1
        if 'Restaurants' and 'Southern' in str(i['categories']):
            Southern_r += i['review_count']
            Southern_c = Southern_c + 1
        if 'Restaurants' and 'Japanese' in str(i['categories']):
            Japanese_r += i['review_count']
            Japanese_c = Japanese_c + 1
        if 'Restaurants' and 'Turkish' in str(i['categories']):
            Turkish_r += i['review_count']
            Turkish_c = Turkish_c + 1
        if 'Restaurants' and 'Hawaiian' in str(i['categories']):
            Hawaiian_r += i['review_count']
            Hawaiian_c = Hawaiian_c + 1
        if 'Restaurants' and 'Lebanese' in str(i['categories']):
            Lebanese_r += i['review_count']
            Lebanese_c = Lebanese_c + 1
        if 'Restaurants' and 'French' in str(i['categories']):
            French_r += i['review_count']
            French_c = French_c + 1
        if 'Restaurants' and 'Filipino' in str(i['categories']):
            Filipino_r += i['review_count']
            Filipino_c = Filipino_c + 1
        if 'Restaurants' and 'Canadian (New)' in str(i['categories']):
            Canadian_new_r += i['review_count']
            Canadian_new_c = Canadian_new_c + 1

ATavg = round(American_traditional_r / American_traditional_c, 2)
Thaiavg = round(Thai_r / Thai_c, 2)
Mediterraneanavg = round(Mediterranean_r / Mediterranean_c, 2)
Greekavg = round(Greek_r / Greek_c, 2)
ANavg = round(American_new_r / American_new_c, 2)
Indianavg = round(Indian_r / Indian_c, 2)
Mexicanavg = round(Mexican_r / Mexican_c, 2)
Taiwaneseavg = round(Taiwanese_r / Taiwanese_c, 2)
Vietnameseavg = round(Vietnamese_r / Vietnamese_c, 2)
Brazilianavg = round(Brazilian_r / Brazilian_c, 2)
Cubanavg = round(Cuban_r / Cuban_c, 2)
Caribbeanavg = round(Caribbean_r / Caribbean_c, 2)
Germanavg = round(German_r / German_c, 2)
AFavg = round(Asian_fusion_r / Asian_fusion_c, 2)
Chineseavg = round(Chinese_r / Chinese_c, 2)
LAavg = round(Latin_american_r / Latin_american_c, 2)
MEavg = round(Middle_eastern_r / Middle_eastern_c, 2)
Italianavg = round(Italian_r / Italian_c, 2)
Southernavg = round(Southern_r / Southern_c, 2)
Japaneseavg = round(Japanese_r / Japanese_c, 2)
Turkishavg = round(Turkish_r / Turkish_c, 2)
Hawaiianavg = round(Hawaiian_r / Hawaiian_c, 2)
Lebaneseavg = round(Lebanese_r / Lebanese_c, 2)
Frenchavg = round(French_r / French_c, 2)
Filipinoavg = round(Filipino_r / Filipino_c, 2)
CNavg = round(Canadian_new_r / Canadian_new_c, 2)

AT = "American (Traditional):" + str(American_traditional_r) + ":" + str(ATavg)
thai = "Thai:" + str(Thai_r) + ":" + str(Thaiavg)
mediterranean = "Mediterranean:" + str(Mediterranean_r) + ":" + str(Mediterraneanavg)
greek = "Greek:" + str(Greek_r) + ":" + str(Greekavg)
AN = "American (New):" + str(American_new_r) + ":" + str(ANavg)
indian = "Indian:" + str(Indian_r) + ":" + str(Indianavg)
mexican = "Mexican:" + str(Mexican_r) + ":" + str(Mexicanavg)
taiwanese = "Taiwanese:" + str(Taiwanese_r) + ":" + str(Taiwaneseavg)
vietnamese = "Vietnamese:" + str(Vietnamese_r) + ":" + str(Vietnameseavg)
brazilian = "Brazilian:" + str(Brazilian_r) + ":" + str(Brazilianavg)
cuban = "Cuban:" + str(Cuban_r) + ":" + str(Cubanavg)
caribbean = "Caribbean:" + str(Caribbean_r) + ":" + str(Caribbeanavg)
german = "German:" + str(German_r) + ":" + str(Germanavg)
asian_fusion = "Asian Fusion:" + str(Asian_fusion_r) + ":" + str(AFavg)
chinese = "Chinese:" + str(Chinese_r) + ":" + str(Chineseavg)
latin_american = "Latin American:" + str(Latin_american_r) + ":" + str(LAavg)
middle_eastern = "Middle Eastern:" + str(Middle_eastern_r) + ":" + str(MEavg)
italian = "Italian:" + str(Italian_r) + ":" + str(Italianavg)
southern = "Southern:" + str(Southern_r) + ":" + str(Southernavg)
japanese = "Japanese:" + str(Japanese_r) + ":" + str(Japaneseavg)
turkish = "Turkish:" + str(Turkish_r) + ":" + str(Turkishavg)
hawaiian = "Hawaiian:" + str(Hawaiian_r) + ":" + str(Hawaiianavg)
lebanese = "Lebanese:" + str(Lebanese_r) + ":" + str(Lebaneseavg)
french = "French:" + str(French_r) + ":" + str(Frenchavg)
filipino = "Filipino:" + str(Filipino_r) + ":" + str(Filipinoavg)
canadian_new = "Canadian (New):" + str(Canadian_new_r) + ":" + str(CNavg)

cuisines1 = [AT, thai, mediterranean, greek, AN, indian, mexican, taiwanese, vietnamese, brazilian, cuban, caribbean,
             german, asian_fusion, chinese, latin_american, middle_eastern, italian, southern, japanese, turkish,
             hawaiian, lebanese, french, filipino, canadian_new]

cuisines1.sort(key=extract_number)
cuisines1.reverse()

text_file = open('Q2_part2.out.txt', 'w')
for cuisine in cuisines1[:10]:
    text_file.write(cuisine + '\n')
text_file.close()

x = np.array(cuisines_x)
y = np.array(cuisines_y)

# plot
plt.subplots(figsize=(10, 10))

plt.bar(x, y)

plt.title("TOP 5 RESTAURANT CATEGORIES")
plt.xlabel("RESTAURANT CATEGORIES")
plt.ylabel("FREQUENCY")

text_file = open('Q2_part3.pdf', 'w')
plt.savefig('Q2_part3.pdf')
text_file.close()

data_file.close()
