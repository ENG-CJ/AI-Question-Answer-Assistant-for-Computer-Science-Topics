import pickle as pkl
import random as rd

with open("intent_model.pkl", "rb") as intent_model:
    data,vector,lr,train_data = pkl.load(intent_model)
responses ={intent['tag']: intent['responses'] for intent in data['intents']}

def predict_question_from_model(text, ai_speaker=None):
    vector.fit_transform(train_data)
    text_vector = vector.transform([text])
    prediction = lr.predict(text_vector)
    intent = prediction[0]
    response = rd.choice(responses[intent])
    if ai_speaker is not None:
        print(f"ai_response: {response}")
        ai_speaker(response)
    else:
        return response
    
