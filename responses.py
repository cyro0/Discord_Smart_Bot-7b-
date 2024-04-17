import llama2_7b

def handle_response(message):
    p_message = message.clean_content.replace('@SmartBot ', '')

    return llama2_7b.generate_response(p_message)