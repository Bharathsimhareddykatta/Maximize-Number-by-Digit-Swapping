from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def maximize_number(first_num, second_num):
    first_digits = list(str(first_num))
    second_digits = sorted(list(str(second_num)), reverse=True)

    second_ptr = 0

    for i in range(len(first_digits)):
        if second_ptr < len(second_digits) and second_digits[second_ptr] > first_digits[i]:
            first_digits[i] = second_digits[second_ptr]
            second_ptr += 1

    return int("".join(first_digits))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maximize_number', methods=['POST'])
def maximize_number_route():
    data = request.get_json()
    first_num = data.get('first_num')
    second_num = data.get('second_num')
    
    if first_num is None or second_num is None:
        return jsonify({"error": "Both 'first_num' and 'second_num' must be provided"}), 400
    
    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except ValueError:
        return jsonify({"error": "Both 'first_num' and 'second_num' must be valid integers"}), 400
    
    result = maximize_number(first_num, second_num)
    
    return jsonify({"maximized_number": result})

if __name__ == '__main__':
    app.run(debug=True)
