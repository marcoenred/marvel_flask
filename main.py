from flask import Flask, render_template
from api_requests import get_data, obtener_personajes
import pprint


app = Flask(__name__)


@app.route("/")
async def home():
    # llamar a la funcion para obtener datos de la api_requests
    try:
        api_data1 = await get_data()

        api_data = await obtener_personajes()
        personajes = api_data.get("data", {}).get('results', [])
        print('data', api_data1.keys())
        return render_template("home.html",
                               api_data=api_data1, personajes=personajes)
    except Exception as e:
        print(f"Error: {e}")
        return render_template("error.html", error_message=str(e))

@app.route("/buscar")
def buscar(starts, numero_personajes):


if __name__ == "__main__":
    app.run(debug=True, port=5000)
