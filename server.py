from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    original_text = data.get("text", "")
    reversed_text = original_text[::-1]
    return jsonify({"original": original_text, "reversed": reversed_text})

if __name__ == '__main__':
    app.run(port=5000)

