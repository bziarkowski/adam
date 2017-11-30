import markovify
import json
import random

text_model = json.loads(open('markov_model.json').read())
text_model = markovify.Text.from_json(json.dumps(text_model))

lines_possible = [6,8,10,12,14,16, 18,20]
lines = lines_possible[random.randint(1, len(lines_possible))]

poem = [text_model.make_short_sentence(50) for i in range(lines)]

toupper_ind = []
tolower_ind = []
for i in range(len(poem)):
    line = poem[i]
    end_line = line[len(line)-1]
    if end_line==',' and i+1<len(poem):
      tolower_ind = tolower_ind + [i+1]
    elif end_line=="." and i+1<len(poem):
      toupper_ind = toupper_ind + [i+1]
    elif end_line.isalpha()==True and i+1<len(poem):
      tolower_ind = tolower_ind + [i + 1]

poem_list = []
for i in range(len(poem)):
    line = poem[i]
    if (i in toupper_ind)==True:
        line = line[0].upper() + line[1:]
        poem_list = poem_list + [line]
    elif (i in tolower_ind)==True:
        line = line[0].lower() + line[1:]
        poem_list = poem_list + [line]
    else:
        poem_list = poem_list + [line]

poem = ' \n '.join(poem_list)
print(poem)


