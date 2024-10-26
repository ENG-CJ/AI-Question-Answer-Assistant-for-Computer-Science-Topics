import pickle as pkl
import random as rd

with open("model.pkl", "rb") as intent_model:
    data,vector,logis,train_data = pkl.load(intent_model)
responses ={intent['tag']: intent['responses'] for intent in data['intents']}

def predict_question_from_model(text,  ai_speaker=None,voice=1):
    # vector.fit_transform(train_data)
    text_vector = vector.transform([text])
    prediction = logis.predict(text_vector)
    intent = prediction[0]
    response = rd.choice(responses[intent])
    if ai_speaker is not None:
        print(f"ai_response: {response}")
        ai_speaker(response,190,1.0,voice)
    else:
        return response
   
