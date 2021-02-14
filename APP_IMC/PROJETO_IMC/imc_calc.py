from PySimpleGUI import PySimpleGUI as sg

def FunctionCalcIMC(Peso, Altura):
  #formula
  CalculoDoIMC = Peso / (Altura * Altura)
  IMC = round(CalculoDoIMC, 2)
  # Condição
  if IMC < 18.5:
    print ("seu imc é ", IMC, "você esta a abaixo do peso")
    return ("seu imc é ", IMC, "você esta a abaixo do peso")

  elif IMC >= 18.5 and IMC <= 24.9:
    print ("seu imc é ", IMC, "você esta no peso normal")
    return ("seu imc é ", IMC, "você esta no peso normal")

  elif IMC >= 25 and IMC <= 29.9:
    print ("seu imc é ", IMC, "você esta sobrepeso")
    return ("seu imc é ", IMC, "você esta sobrepeso")
  
  elif IMC >= 30 and IMC <= 34.9:
    print ("seu imc é ", IMC, "você esta com obesidade grau 1")
    return ("seu imc é ", IMC, "você esta com obesidade grau 1")

  elif IMC >= 35 and IMC <= 39.9:
    print ("seu imc é ", IMC, "você esta com obesidade grau 2")
    return

  else :
    print ("seu imc é ", IMC, "você esta com obesidade grau 3 ou morbida")
    return ("seu imc é ", IMC, "você esta com obesidade grau 3 ou morbida")

sg.theme("Reddit")

layout = [
    [sg.Text("Peso (kg):"), sg.Input(key="peso")],
    [sg.Text("Altura (cm):"), sg.Input(key="altura")],
    [sg.Text("------------------------------------------------------------------------------------------------------")],
    [sg.Text("Exemplo:")],
    [sg.Text("Peso: 70")],
    [sg.Text("Altura: 1.70")],
    [sg.Button("Calcular")]
]

janela = sg.Window("IMC", layout)


while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
      break
    if eventos == "Calcular":
      sg.popup(FunctionCalcIMC(int(valores["peso"]), float(valores["altura"])))
      print(FunctionCalcIMC(int(valores["peso"]), float(valores["altura"])))