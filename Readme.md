# adam
`adam` is a polish poetry generator that uses Markov Chains. Markov chains were generated using polish poems scraped from web (250000 lines of text). This corpus is stored in `poems.txt`.
You can try `adam` [here](http://bziarkowski.pl/adam/).
See also [twitter bot](https://twitter.com/wierszeadama).
# Installation
In terminal.
```
git clone https://github.com/bziarkowski/adam.git
cd adam
```
Install Python requirements.
```
pip install -r requirements.txt
```
Now it should be ready to use.

# Generate poems
To generate poems run:
```
python generate_poems.py
```
# Run app
To start `adam` app:
```
python app.py
```
After this operation the app will be available on port 5000.
Simply open your browser and type `localhost:5000`