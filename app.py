from flask import Flask, render_template, request, jsonify
import json
import markovify


app = Flask(__name__)

#load markov models
model = json.loads(open('markov_model.json').read())
text_model = markovify.Text.from_json(json.dumps(model))

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/gen', methods = ['POST'])
def background_process():
    lines = int(request.form.get('lines'))
    if request.form['text'] != '':
        text = request.form['text']
        poem = [text_model.make_sentence_with_start(text) for i in range(lines)]
        toupper_ind = []
        tolower_ind = []
        for i in range(len(poem)):
            line = poem[i]
            end_line = line[len(line) - 1]
            if end_line == ',' and i + 1 < len(poem):
                tolower_ind = tolower_ind + [i + 1]
            elif end_line == "." and i + 1 < len(poem):
                toupper_ind = toupper_ind + [i + 1]
            elif end_line.isalpha() == True and i + 1 < len(poem):
                tolower_ind = tolower_ind + [i + 1]
            poem_list = []
            for i in range(len(poem)):
                line = poem[i]
                if (i in toupper_ind) == True:
                    line = line[0].upper() + line[1:]
                    poem_list = poem_list + [line]
                elif (i in tolower_ind) == True:
                    line = line[0].lower() + line[1:]
                    poem_list = poem_list + [line]
                else:
                    poem_list = poem_list + [line]
        poem = ' \n '.join(poem_list)
        return jsonify(result = poem)
    elif request.form['text'] == '':
        poem = [text_model.make_short_sentence(50) for i in range(lines)]
        toupper_ind = []
        tolower_ind = []
        for i in range(len(poem)):
            line = poem[i]
            end_line = line[len(line) - 1]
            if end_line == ',' and i + 1 < len(poem):
                tolower_ind = tolower_ind + [i + 1]
            elif end_line == "." and i + 1 < len(poem):
                toupper_ind = toupper_ind + [i + 1]
            elif end_line.isalpha() == True and i + 1 < len(poem):
                tolower_ind = tolower_ind + [i + 1]
            poem_list = []
            for i in range(len(poem)):
                line = poem[i]
                if (i in toupper_ind) == True:
                    line = line[0].upper() + line[1:]
                    poem_list = poem_list + [line]
                elif (i in tolower_ind) == True:
                    line = line[0].lower() + line[1:]
                    poem_list = poem_list + [line]
                else:
                    poem_list = poem_list + [line]
        poem = ' <br> '.join(poem_list)
        return jsonify(result=poem)



if __name__ == "__main__":
    app.run()