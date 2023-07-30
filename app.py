from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/cep/<cep>', methods=['GET'])
def get_address(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({'message': 'CEP not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
