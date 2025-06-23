# Currency_converter

Convertidor de Divisas / Currency Converter

📖 Descripción / Description
Este proyecto es una aplicación de escritorio en Python que permite convertir montos entre distintas monedas usando la API de ExchangeRate‑API.
This desktop app in Python lets you convert amounts between world currencies using the ExchangeRate‑API.

🛠️ Tecnologías / Technologies
- Python ≥ 3.7
- Tkinter (Interfaz gráfica)
- Requests (Llamadas HTTP a la API)

🚀 Características / Features
- ✅ Conversión en tiempo real usando la moneda From definida por el usuario.
- ✅ Validación de códigos ISO de moneda (solo 3 letras, A–Z).
- ✅ Botones de ayuda “?” con explicación de códigos ISO (USD, EUR, JPY, CHF, GBP).
- ✅ Mensajes de error claros (cantidad inválida, tasa no disponible, fallo de API).

📦 Instalación / Installation
1. Clonar el repositorio:
   git clone https://github.com/tu_usuario/currency-converter.git
   cd currency-converter
2. (Opcional) Crear y activar un entorno virtual:
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
3. Instalar dependencias:
   pip install -r requirements.txt

⚙️ Uso / Usage
python currency_converter.py
1. Escribe la cantidad en Amount.
2. Introduce la moneda de origen en From (ej. USD).
3. Introduce la moneda de destino en To (ej. EUR).
4. Haz clic en Convert.

📄 Estructura del Proyecto / Project Structure
currency-converter/
├── currency_converter.py
├── requirements.txt
└── README.md

📝 Documentación / Documentation
- Cada función documentada con docstrings.
- Mensajes de validación y ayuda en la interfaz.

🔧 Desarrollo / Development
Para colaborar:
1. Haz un fork.
2. Crea una rama: git checkout -b feature/nueva-funcionalidad.
3. Realiza tus cambios y commitea: git commit -m "Añade validación extra".
4. Empuja tu rama y abre un Pull Request.

🧪 Tests / Tests
Si añades tests, ejecútalos con:
pytest

🤝 Contribuciones / Contributing
¡Contribuciones bienvenidas! Revisa CONTRIBUTING.md para más detalles.

📜 Licencia / License
MIT License

✉️ Contacto / Contact
- Hely Camargo – helycamargo115@gmail.com
- GitHub: HelyCamargo115
