from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)


@app.route('/')
def get_event():
    #get the api key from ticketmaster developer website
    api_key = "Zno3Ua2Uc6W4Am1IgDrW9osB2H6dnZct"

    #create the list for containing events dictionaries. 
    event_list = []
    

    for i in range(2):  # you can change the number in range(num) for how many pages you want
        
        #get the json data 
        event_data = fetch_event_details(api_key,i)

        # Check if the response is an error message
        if isinstance(event_data, str):  
                return make_response(jsonify({'error': event_data}), 403)
        
            
        #get the events list in json file 
        events = event_data.get("_embedded",{}).get("events", [])

        #create the dictionary for each event by traversing all the events
        for event in events:    

            #create the new dictionary
            event_info = {}

            #get the event name, data, url
            event_info['event_name'] = event.get('name')
            event_info['event_date'] = event.get('dates', {}).get('start', {}).get('localDate', 'Date not available')
            event_info['event_url'] = event.get('url', 'URL not available')

            #get the "venues" list for event
            venues = event.get("_embedded", {}).get("venues", [])

            #get the "city" information in the list
            for venue in venues:

                #get the city name for the event and check the city is matched
                city = venue.get("city", {}).get("name", "")
                if city == "Minneapolis":
                    event_info['venue'] = venue.get('name', 'Venue not available')
                    event_info['city'] = city

                    # get the image url 
                    images = event.get('images', [])
                    if images and len(images) > 3:
                        event_info['image_url'] = images[8].get('url', 'No image available')
                    
                    
                    # if the city is mateched, the dictionary is added to the list 'event_list'
                    if event_info.get('event_name') and event_info.get('venue'):
                        event_list.append(event_info)       



    return make_response(jsonify({"events": event_list}), 200)




# get the api key and page number
def fetch_event_details(api_key,page):

    #url for events 
    url = f"https://app.ticketmaster.com/discovery/v2/events?apikey={api_key}&locale=*&page={page}"

    #request
    response = requests.get(url)

    #return the json if the data is successfully retrieved. 
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to retrieve events."

if __name__ == '__main__':
    app.run(debug=True)
