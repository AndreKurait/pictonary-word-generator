from flask import Flask
app = Flask(__name__)

@app.route('/<string:cat>/<int:num>')
def getWord(cat,num):
    words = [line.strip() for line in open('word-lists/' + cat + '.txt')]
    word = words[num % len(words)]
    return '<center><h1>'+word+'</h1></center>'
if __name__ == '__main__':
    app.run()