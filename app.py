from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'secret-key'

WORDS = ["apple","banana","cherry","mango","litchi","orange","grape"]
HANGMAN_ART = {
    0:("   ",
       "   ",
       "   "),
    1:(" 0  ",
       "   ",
       "   "),
    2:(" 0  ",
       " |  ",
       "   "),
    3:(" 0  ",
       "/|  ",
       "   "),
    4:(" 0  ",
       "/|\\ ",
       "   "),
    5:(" 0  ",
       "/|\\ ",
       "/   "),
    6:(" 0  ",
       "/|\\  ",
       "/ \\  ")
}

MAX_WRONG = 6

def start_game():
    word = random.choice(WORDS)
    session['answer'] = word
    session['hints'] = ['_'] * len(word)
    session['wrong_guesses'] = []
    session['wrong_answers'] = 0

@app.route('/')
def index():
    if 'answer' not in session:
        start_game()
    return render_template('index.html')

@app.route('/state')
def state():
    wrong = session.get('wrong_answers',0)
    return jsonify({
        'hints': ''.join(session.get('hints', [])),
        'wrong_guesses': session.get('wrong_guesses', []),
        'wrong_answers': wrong,
        'hangman': HANGMAN_ART[wrong]
    })

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json(force=True)
    ch = data.get('guess','').lower()
    answer = session['answer']
    hints = session['hints']
    wrong_guesses = session['wrong_guesses']
    wrong_answers = session['wrong_answers']
    message = ''
    if len(ch) != 1 or not ch.isalpha():
        message = 'invalid'
    elif ch in answer:
        for i, letter in enumerate(answer):
            if letter == ch:
                hints[i] = ch
        if '_' not in hints:
            message = 'win'
    else:
        if ch not in wrong_guesses:
            wrong_guesses.append(ch)
            wrong_answers += 1
            session['wrong_answers'] = wrong_answers
        if wrong_answers >= MAX_WRONG:
            message = 'lose'
    session['hints'] = hints
    session['wrong_guesses'] = wrong_guesses
    resp = {
        'hints': ''.join(hints),
        'wrong_guesses': wrong_guesses,
        'wrong_answers': wrong_answers,
        'hangman': HANGMAN_ART[wrong_answers],
        'message': message
    }
    if message == 'lose':
        resp['answer'] = answer
    return jsonify(resp)

@app.route('/restart', methods=['POST'])
def restart():
    start_game()
    return jsonify({'status':'restarted'})

if __name__ == '__main__':
    app.run(debug=True)
