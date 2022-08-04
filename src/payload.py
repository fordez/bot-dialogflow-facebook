
def payloadFacebok(data) -> dict:
        try:    
                payload = {}
                data = data.entry[0]['messaging'][0]
                payload['sender_id'] = data['sender']['id']
                payload['recipient_id'] = data['recipient']['id']
                payload['message_id'] = data['message']['mid']
                try:
                        if data['message']['text']:
                                payload['message'] = data['message']['text']
                                payload['message_type'] = 'text'
                                
                except:
                        if data['message']['attachments'][0]['type'] == 'location':
                                data = data['message']['attachments'][0]['payload']['coordinates']
                                payload['latitude'] = data['lat']
                                payload['longitude'] = data['long']
                                payload['message_type'] = 'location'
                               
                        else:
                                data = data['message']['attachments'][0]
                                payload['url'] = data['payload']['url']
                                payload['type'] = data['type']
                                payload['message_type'] = 'media'
                return payload                    
                                
                
        except:
                print(data)

    