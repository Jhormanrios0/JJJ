import re
import random
from id3 import Id3Estimator, export_graphviz

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def messange_probability(user_message, recognized_words, single_response=False, required_words=[]):
    messange_certainty = 0
    has_required_words = True 

    for word in user_message:
        if word in recognized_words:
            messange_certainty += 1

    percentage = float(messange_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break 

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = messange_probability(message, list_of_words, single_response, required_words)

    response('Bienvenido',['Hola', 'Buenos dias', 'Buenas tardes', 'Buenas noches'], single_response=True)
    response('¿En que te puedo ayudar?', ['Necesito ayuda'], single_response=True)
    response('¿Que sintomas tienes?', ['Estoy enfermo', 'Enfermedad'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['¿Puedes decirlo de nuevo?', 'No estoy segura de lo que quieres'][random.randrange(3)]
    return "Bot: " + response

while True:
    highest_prob = {}
    print("Bot: ", end="")
    user_message = input()
    response = get_response(user_message)
    if highest_prob[response] < 1:
        print(unknown())
    else:
        print(response)
        
# Definimos nuestra base de conocimiento de enfermedades y síntomas
enfermedades = [
    {'enfermedad': 'Resfriado común', 'sintomas': ['Tos', 'Estornudos', 'Secreción nasal']},
    {'enfermedad': 'Gripe', 'sintomas': ['Fiebre', 'Dolor de cabeza', 'Dolor muscular']},
    {'enfermedad': 'COVID-19', 'sintomas': ['Fiebre', 'Tos seca', 'Fatiga']}
    
]

estimator = Id3Estimator()       
X = [e['sintomas'] for e in enfermedades]
y = [e['enfermedad'] for e in enfermedades]
estimator.fit(X, y)

def predecir_enfermedad(sintomas):
    prediccion = estimator.predict([sintomas])[0]
    return prediccion

score = clf.score(X_test, y_test)
print("Precisión: ", score)

def chatbot():
    print("¡Bienvenido al chatbot de enfermedades!")
    print("Por favor, ingrese sus síntomas (separados por comas):")
    while True:
        sintomas = input("> ")
        sintomas = [sintoma.strip().lower() for sintoma in sintomas.split(",")]
        enfermedad = predecir_enfermedad(sintomas)
        print("Según los síntomas ingresados, usted podría tener:", enfermedad)
        print("¿Hay algo más en lo que pueda ayudarlo?")    
