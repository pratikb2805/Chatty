import os, sys
from wit import Wit
sys.path.insert(0,'/media/pratik/Programs/devops/webd/projects/chatbot/bot/')

from utils import *

class Bot(Wit):
    def __init__(self, access_token = 'OTZ4HIQAX47G7YGIXS43IQ6C5DL5DIZG', name = "Chatty", userName = "User"):
        super(Bot, self).__init__(access_token)
        self.client = Wit(access_token)
        self.entities = ['bye', 'greetings', 'location', 'math_expression', 'notable_person', 'search_query', 'temperature', 'thanks', 'url', 'wikipedia_search_query', 'wolfram_search_query']
        self.name = name
        self.user = userName

    def get_trait(self, response: dict):
        if len(response['traits']) == 0:
            return None 
        else:
            trait = list(response['traits'].keys())[0]
            return trait
    
    def get_intent(self, response: dict):
        if len(response['intents']) == 0:
            return None
        else:
            return response['intents'][0]['name']

    def get_entity(self, response: dict):
        if len(response['entities']) == 0:
            return None
        else:
            key = list(response['entities'].keys())[0]
            ent_dict = response['entities'][key][0]
            entity_name = ent_dict['name']
            entity_body = ent_dict['value']
            return {'name': entity_name, 'value':entity_body}

    
    def responser(self, msg):
        return self.message(msg)
    
    def resolver(self, response):
        trait = self.get_trait(response)
        if trait is not None:
            if trait == 'wit$bye':
                return "Bye, take care"
            else:
                return starter()
        
        else:
            intent = self.get_intent(response)
            try:
                entity = self.get_entity(response)['value']
            except:
                entity = None
            if intent == 'weatherSearch':
                return get_weather()
            elif intent == 'temperatureSearch':
                return get_temperature()
            elif intent == 'search':
                return get_wikidata(entity)
            elif intent == 'botQuery':
                return f"My name is {self.name}"
            elif intent == 'nameQuery':
                return f"Your name is {self.user}"
            else:
                return "Sorry I couldnt understand your question"

    def __call__(self, msg):
        resp = self.responser(msg)
        resolved_response = self.resolver(resp)
        return resolved_response

    def __str__(self):
        return f"{self.name}-The Bot"

if __name__ == "__main__":
    bot = Bot(userName="Pratik")
    print(bot)