from flask import Flask, request, render_template_string
 
app = Flask(__name__)
 
 
@app.route('/')
def home():
    return '<h1>Bienvenido a Flask Vuln App</h1><p>Prueba /hello?name=test</p>'
 
 
@app.route('/hello')
def hello():
    name = request.args.get('name', 'mundo')
    # NOTA: esto es intencionalmente vulnerable a XSS para fines de
    # laboratorio (DevSecOps / DAST con OWASP ZAP). No usar en producción.
    template = f'<h1>Hola, {name}!</h1>'
    return render_template_string(template)
 
 
@app.route('/health')
def health():
    return {'status': 'ok'}, 200
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
