import sys

text_file_path = sys.argv[1]

data_file = open(text_file_path)

vertices_list = []
edge_count = 0

for line in data_file:
    edge_count = edge_count + 1
    word = line.split(" ")
    if vertices_list.count(word[0]) == 0:
        vertices_list.append(word[0])

avg_node_degree = round(((edge_count / len(vertices_list)) * 2), 2)

text_file = open('Q4.out.txt', 'w')
text_file.write(str(len(vertices_list)) + ' ' + str(edge_count) + '\n')
text_file.write(str(avg_node_degree) + '\n')
text_file.close()

data_file.close()


