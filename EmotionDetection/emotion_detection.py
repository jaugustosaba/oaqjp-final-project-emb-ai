'''
Emotion Predict function of the Watson NLP Library.
'''
import requests
import json


def emotion_detector(text_to_analyze):
    '''run emotion detection using the appropriate Emotion Detection function'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(url, json=payload, headers=headers).text
    obj = json.loads(resp)
    emotions = obj['emotionPredictions'][0]['emotion']
    result = {}
    dominant = None
    for emotion, score in emotions.items():
        result[emotion] = score
        if dominant is None or score > emotions[dominant]:
            dominant = emotion
    result['dominant_emotion'] = dominant
    return result