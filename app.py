from flask import Flask, request, jsonify, render_template
from functional import get_next_location
app = Flask(__name__)

def my_function(input1, input2):
    """ Example function to process inputs and return an output """
    return f"Processed: {input1} and {input2}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    input1 = data.get("input1", "")
    try:
        input2 = int(data.get("input2", ""))
    except e as e:
        print("Invalid")
    print(input1,input2)
    result = get_next_location(input1,input2)
    print(result)
    return jsonify({"result": result})

if __name__ == '__main__':
    import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Azure-assigned port
    app.run(host='0.0.0.0', port=port)
