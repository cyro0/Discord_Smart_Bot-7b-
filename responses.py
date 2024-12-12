from gemma2_2b import generate_response, delete_context

def handle_response(message):
    p_message = message.clean_content.replace('@SmartBot ', '')

    if p_message == '/delc':
        delete_context()
        return("|Context deleted|")
    else:
        return generate_response(p_message) 