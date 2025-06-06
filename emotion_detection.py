
import requests
import json

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json, timeout=30)
    response.raise_for_status()
    response_dict = json.loads(response.text)
    emotions = response_dict['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return result

    
    # try:
    #     response = requests.post(url, headers=headers, json=input_json, timeout=30)
    #     response.raise_for_status()
    #     response_dict = json.loads(response.text)
    #     emotions = response_dict['emotionPredictions'][0]['emotion']
    #     dominant_emotion = max(emotions, key=emotions.get)
    #     result = {
    #         'anger': emotions.get('anger', 0),
    #         'disgust': emotions.get('disgust', 0),
    #         'fear': emotions.get('fear', 0),
    #         'joy': emotions.get('joy', 0),
    #         'sadness': emotions.get('sadness', 0),
    #         'dominant_emotion': dominant_emotion
    #     }

    #     return result
    # except Exception as e:
    #     print("Error during request:", e)
    #     return None
