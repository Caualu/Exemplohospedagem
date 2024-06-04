# fça um sistema que receba a altura e peso de  uma pessoa e calcule o img de uma pessoa
import dearpygui.dearpygui as dpg


dpg.create_context()


def IMC():
    
    altura_imc = dpg.get_value("altura_imc")
    peso_imc = dpg.get_value("peso_imc")
   
    
    try:
       
     peso_imc = float(peso_imc)
     altura_imc = float(altura_imc)
     imc = peso_imc / (altura_imc * altura_imc)

       
     dpg.set_value("resultado", f"IMC final:{imc:,.2f}")
    except ValueError:
       
     dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")



dpg.create_viewport(title='Calculadora de imc', width=700, height=300)


with dpg.window(label="Calculadora IMC", width=600, height=300):
   
    dpg.add_input_text(label="altura_imc:", tag="altura_imc")
   
    dpg.add_input_text(label="peso_imc:", tag="peso_imc")
    
    dpg.add_button(label="Calcular imc", callback=IMC)
   
    dpg.add_text("", tag="resultado")


dpg.setup_dearpygui()
dpg.show_viewport()

dpg.start_dearpygui()
dpg.destroy_context()
