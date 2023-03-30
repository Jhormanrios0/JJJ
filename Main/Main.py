import re
import ramdom

def get_response(user_input):
	split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
     response = check_all_messages(split_message)
     return response

def messange_probability(user_message, recognized_words,single_response=False, required_word[]):
    messange_certainty = 0
    has_required_words = True 



    for word in user_message
       if word in recognized_words:
       	  messange_certainty +=1


    percentage = float(messange_certainty) / float (len(recognized_words))

    for word in required_word
       if word not in user_message:
       	   has_required_words = False
       	   break 
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
    	return 0

    def check_all_messages(messange):
    	highest_prob ={}


    	def response(bot_response, List_of_words, single_response = False, required_word[]):
    		nonlocal highest_prob
    		highest_prob[bot_response] = messange_probability(message,List_of_words, single_response, required_word)

        response('Bienvenido',['Hola', 'Buenos dias' , 'Buenas tardes', 'Buenas noches'] single_response = True)
        response('¿En que te puedo ayudar?',['Necesito ayuda'], single_response = True)
        response('¿Que sintomas tienes?', ['Estoy enfermo','Enfermedad'], single_response=True )
        

        best_match = max(highest_prob, key=highest_prob.get)
        print(highest_prob)


        return unknown() if highest_prob[best_match] < 1  else best_match


def unknown():
	response = ['¿Puedes decirlo de nuevo?','No estoy segura de lo que quieres'][ramdom.randrange(3)]



while true:
	print("Bot:" + get_response(input('You: ')))
#cambios
