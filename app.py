from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# --- CONFIGURAÇÃO ---
API_KEY = "SUA_CHAVE_AQUI"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@app.route('/convert', methods=['GET'])
def convert_currency():
    """
    Endpoint da API para converter moedas.
    Recebe os parâmetros via query string: amount, from_curr, to_curr
    """
    amount_str = request.args.get('amount')
    from_curr = request.args.get('from_curr')
    to_curr = request.args.get('to_curr')

    if not all([amount_str, from_curr, to_curr]):
        return jsonify({'error': 'Parâmetros ausentes: amount, from_curr e to_curr são obrigatórios.'}), 400

    try:
        amount = float(amount_str)
    except ValueError:
        return jsonify({'error': 'O valor (amount) deve ser um número válido.'}), 400

    try:
        url = BASE_URL + from_curr
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('result') == 'success':
            conversion_rate = data.get('conversion_rates', {}).get(to_curr)
            if conversion_rate is None:
                return jsonify({'error': f'A moeda de destino "{to_curr}" não foi encontrada.'}), 404
            
            converted_amount = amount * conversion_rate
            
            return jsonify({
                'original_amount': amount,
                'from_currency': from_curr,
                'to_currency': to_curr,
                'conversion_rate': conversion_rate,
                'converted_amount': converted_amount
            })
        else:
            error_message = data.get('error-type', 'Erro desconhecido na API de câmbio.')
            return jsonify({'error': f'Erro na API de câmbio: {error_message}'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Erro de conexão com a API de câmbio: {e}'}), 503
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro inesperado no servidor: {e}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)