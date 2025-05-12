from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                resultado = "Las notas deben estar entre 10 y 70."
            elif not (0 <= asistencia <= 100):
                resultado = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = (nota1 + nota2 + nota3) / 3
                estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
                resultado = f"Promedio: {promedio:.2f} | Asistencia: {asistencia:.0f}% → {estado}"

        except ValueError:
            resultado = "Por favor, ingresa valores válidos."

    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        resultado = {
            'nombre': nombre_largo,
            'longitud': len(nombre_largo)
        }

    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
