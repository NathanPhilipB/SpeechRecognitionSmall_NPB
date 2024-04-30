from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/xxxxxx', methods=['POST'])
def answer_question():
    if request.method == 'POST':
        # Receive JSON data from the client containing the question
        question_json = request.json

        # Extract the question from the JSON data
        question = question_json.get('question', '')

        # Process the question using the LLM to get the answer
        answer = ("kill yourself") #LLM(question)

        # Return the answer to the client as JSON response
        return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)