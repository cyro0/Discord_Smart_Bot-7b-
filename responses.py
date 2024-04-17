from .llama2_7b import generate_response

def handle_response(message):
    p_message = message.clean_content.replace('@SmartBot ', '')

    return generate_response(p_message)