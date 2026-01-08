from .motor_triaje import clasificar_evento
from .notificaciones import enviar_notificacion

def procesar_alerta(data: dict):
    """
    Procesa una alerta recibida desde un casco o chaleco inteligente.
    """
    # 1. Clasificar la gravedad del evento
    nivel = clasificar_evento(data)

    # 2. Preparar mensaje
    mensaje = {
        "trabajador_id": data.get("trabajador_id"),
        "tipo_alerta": data.get("tipo"),
        "nivel_gravedad": nivel,
        "signos_vitales": data.get("signos_vitales", {}),
        "ubicacion": data.get("ubicacion", {})
    }

    # 3. Enviar notificación al dashboard
    enviar_notificacion(mensaje)

    return {
        "status": "procesado",
        "nivel_gravedad": nivel
    }
