import re

def process_message(message, response_array, response):

    list_message = re.findall(r"[\w']+|[.,¡¿!?;]", message.lower())
    
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1
    
    
    print(score, response)  
    return [score, response]

def get_response(message):
    response_list = [
        process_message(message, ['hola', 'hey', 'buenas', 'holis'], '¡Hola! ¿Cómo estás? Soy el bot de Total Look, ¿en qué puedo ayudarte hoy?'),
        process_message(message, ['bye', 'chau', 'adios', 'hasta', 'luego'], 'Chau, ¡que tengas un excelente día!'),
        process_message(message, ['como', 'còmo', 'estàs', 'estas', 'vos'], 'Estoy bien, gracias por preguntar. ¿Y tú?'),
        process_message(message, ['cuàl', 'es', 'tu', 'nombre', 'còmo', 'te', 'llamas'], 'Me llamo Fran, soy el asistente de Total Look'),
        process_message(message, ['me', 'puedes', 'ayudar', 'help'], '¡Claro! ¿Cómo puedo ayudarte con tu compra en Total Look?'),
        process_message(message, ['ropa', 'camisa', 'pantalón', 'vestido', 'faldas'], 'En Total Look tenemos una gran variedad de ropa moderna para hombres y mujeres. ¿Te interesa algo en particular?'),
        process_message(message, ['envío', 'entrega', 'enviar', 'envíos'], 'Ofrecemos envíos a todo el país. ¡Puedes recibir tu pedido directamente en casa!'),
        process_message(message, ['ofertas', 'descuentos', 'promociones'], '¡Claro! Tenemos promociones especiales cada mes. Visita nuestra sección de ofertas en el sitio web para conocer las más recientes.'),
        process_message(message, ['horario', 'atención', 'tienda'], 'Estamos disponibles para atención en línea las 24 horas del día, los 7 días de la semana. ¡Compra cuando quieras!'),
        process_message(message, ['tamaño', 'tallas'], 'En Total Look tenemos una amplia gama de tallas, desde S hasta XXL. ¿Te gustaría saber más sobre alguna prenda en particular?'),
        process_message(message, ['cómo', 'comprar', 'realizar pedido'], 'Puedes realizar tu pedido directamente desde nuestro sitio web. Solo selecciona los productos que deseas, agrega tu dirección de envío y paga de manera segura.')
    ]
    
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])
        
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]
    
    if winning_response == 0:
        bot_response = 'No entiendo lo que escribiste, ¿puedes intentar con algo diferente?'
    else:
        bot_response = matching_response[1]
    
    print('La respuesta del Bot:', bot_response)
    return bot_response
