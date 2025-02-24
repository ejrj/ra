import streamlit as st

def calcular_costos(
    valor_adquisicion, vida_util, valor_rescate, seguro,
    impuestos, almacenaje, interes_anual, consumo_combustible,
    costo_combustible, lubricantes, grasas, mantenimiento,
    filtros, neumaticos, piezas_desgaste, salario_operador,
    costos_adicionales, horas_anuales
):
    # Cálculo de costos de posesión
    costo_depreciacion = (valor_adquisicion - valor_rescate) / vida_util
    costo_anual_posesion = costo_depreciacion + seguro + impuestos + almacenaje + (valor_adquisicion * interes_anual / 100)
    costo_por_hora_posesion = costo_anual_posesion / horas_anuales

    # Cálculo de costos de operación
    costo_hora_combustible = consumo_combustible * costo_combustible
    costo_hora_mantenimiento = mantenimiento / vida_util
    costo_hora_repuestos = filtros + neumaticos + piezas_desgaste
    costo_hora_operador = salario_operador + costos_adicionales

    costo_por_hora_operacion = costo_hora_combustible + lubricantes + grasas + costo_hora_mantenimiento + costo_hora_repuestos + costo_hora_operador
    costo_total_por_hora = costo_por_hora_posesion + costo_por_hora_operacion
    costo_total_por_dia = costo_total_por_hora * (horas_anuales / 365)

    return costo_total_por_hora, costo_total_por_dia

# Interfaz en Streamlit
st.title("Calculadora de Costos de Payloader")

valor_adquisicion = st.number_input("Valor de adquisición ($)", min_value=0.0, step=1000.0)
vida_util = st.number_input("Vida útil (horas)", min_value=1, step=100)
valor_rescate = st.number_input("Valor de rescate ($)", min_value=0.0, step=100.0)
seguro = st.number_input("Costo anual del seguro ($)", min_value=0.0, step=100.0)
impuestos = st.number_input("Impuestos anuales ($)", min_value=0.0, step=100.0)
almacenaje = st.number_input("Costo anual de almacenaje ($)", min_value=0.0, step=100.0)
interes_anual = st.number_input("Tasa de interés anual (%)", min_value=0.0, step=0.1)
consumo_combustible = st.number_input("Consumo de combustible (litros/hora)", min_value=0.0, step=0.1)
costo_combustible = st.number_input("Costo del combustible ($/litro)", min_value=0.0, step=0.1)
lubricantes = st.number_input("Costo de lubricantes ($/hora)", min_value=0.0, step=0.1)
grasas = st.number_input("Costo de grasas ($/hora)", min_value=0.0, step=0.1)
mantenimiento = st.number_input("Costo total de mantenimiento y reparaciones ($)", min_value=0.0, step=100.0)
filtros = st.number_input("Costo de filtros ($/hora)", min_value=0.0, step=0.1)
neumaticos = st.number_input("Costo de neumáticos u orugas ($/hora)", min_value=0.0, step=0.1)
piezas_desgaste = st.number_input("Costo de piezas de desgaste ($/hora)", min_value=0.0, step=0.1)
salario_operador = st.number_input("Salario del operador ($/hora)", min_value=0.0, step=1.0)
costos_adicionales = st.number_input("Costos adicionales del operador ($/hora)", min_value=0.0, step=0.1)
horas_anuales = st.number_input("Horas anuales de operación", min_value=1, step=100)

if st.button("Calcular Costos"):
    costo_hora, costo_dia = calcular_costos(
        valor_adquisicion, vida_util, valor_rescate, seguro,
        impuestos, almacenaje, interes_anual, consumo_combustible,
        costo_combustible, lubricantes, grasas, mantenimiento,
        filtros, neumaticos, piezas_desgaste, salario_operador,
        costos_adicionales, horas_anuales
    )
    st.write(f"Costo total por hora: ${costo_hora:.2f}")
    st.write(f"Costo total por día: ${costo_dia:.2f}")