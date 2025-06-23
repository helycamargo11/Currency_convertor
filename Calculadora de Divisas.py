import requests
from tkinter import *
from tkinter import messagebox

API_KEY = "97d644b58cc4eaa3e22186a7"

def validate_currency(New_Value):
    return New_Value.isalpha() and len(New_Value) == 3

def show_help():
    messagebox.showinfo(
        "Formato de moneda",
        "Introduce la moneda en 3 letras ISO:\n"
        "USD - Dólar estadounidense\n"
        "EUR - Euro\n"
        "JPY - Yen japonés\n"
        "CHF - Franco suizo\n"
        "GBP - Libra esterlina")

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = currency_from.get().upper().strip()
        to_currency = currency_to.get().upper().strip()

        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        if data['result'] != 'success':
            raise ValueError("API Error")
        rate = data['conversion_rates'].get(to_currency)
        if rate is None:
            raise KeyError(f"Not available for {to_currency}.")
        converted = amount * rate
        result.set(f"{converted:.2f} {to_currency}")
    except ValueError:
        result.set("Cantidad inválida.")
    except KeyError as e:
        result.set(str(e))
    except Exception:
        result.set("Error en API o formato.")        

root = Tk()
root.title("Currency Converter")
root.resizable(False, False)

entry_amount = StringVar()
currency_from = StringVar()
currency_to = StringVar()
result = StringVar()

vcmd = (root.register(validate_currency), '%P')

Label(root, text='Amount:').grid(row=0, column=0, padx=5, pady=5, sticky="e")
Entry(root, justify="center",textvariable=entry_amount).grid(row=0, column=1, padx=5, pady=5, sticky="e") #Cantidad
Label(root, text='From:').grid(row=1, column=0, padx=5, pady=5, sticky="e")
Entry(root, justify="center",textvariable=currency_from).grid(row=1, column=1, padx=5, pady=5, sticky="e") #Desde:
Button(root, text='?', command=show_help, width=2).grid(row=1, column=2)
Label(root, text='To:').grid(row=2, column=0, padx=5, pady=5, sticky="e")
Entry(root, justify="center",textvariable=currency_to).grid(row=2, column=1, padx=5, pady=5, sticky="e") #A:
Button(root, text='?', command=show_help, width=2).grid(row=2, column=2)
Label(root, text="").grid(row=3, column=0, padx=5, pady=5, sticky="e")
Label(root, text='Result:').grid(row=4, column=0, padx=5, pady=5, sticky="e")
Entry(root, justify="center",textvariable=result, state=("readonly")).grid(row=4, column=1, padx=5, pady=5, sticky="e") #Resultado
Button(root, text="Convert", command = convert_currency, justify="center").grid(row=5, column=1, padx=5, pady=5)


root.mainloop()