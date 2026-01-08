from ia.inferencia.predictor_riesgo import predecir_riesgo_fatiga

def clasificar_evento(data: dict) -> str:
    """
    Clasifica la gravedad de un evento basado en signos vitales, tipo de alerta
    y el predictor de riesgo de fatiga.
    """

    tipo = data.get("tipo")
    signos = data.get("signos_vitales", {})

    # Si es una caída, prioridad alta directa
    if tipo == "caida":
        return "alta"

    # Usar el predictor de riesgo de fatiga
    resultado_ia = predecir_riesgo_fatiga(signos)
    riesgo = resultado_ia.get("riesgo")

    if riesgo == "alto":
        return "critica"
    if riesgo == "medio":
        return "alta"

    return "normal"
