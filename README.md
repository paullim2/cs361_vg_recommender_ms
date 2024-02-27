# Setup
1. Download 'vg_recommender_microservice.py' and store in the same folder of your HTML file.
2. Install Flask from your Python library.
3. Open the microservice file, and under 'def index()', change HTML string to be equal to your HTML file name. Save.
4. Run 'vg_recommender_microservice.py'.
5. Open http://localhost:8000

# Communication Contract
## Requesting Data from the Microservice
1. In your webapp file in the same tag of your forms to select genre, length, and platform(s) preferences, add the following:
   action="/submit" method="post"

   An example tag (and by proxy example call) could be: &lt;form id="gameForm" action="/submit" method="post"&gt;

   Now when the user selects their videogame preferences and hits submit, these values will be passed to the Flask endpoint /submit. 

## Receiving Data from the Microservice
1. In the JavaScript portion of your HTML, define the following elements in your fetch command:
      * url = '/submit'
      * method = 'POST'
2. The response comes in this format: ['title', 'cost', 'length', ['platform 1', 'platform 2', ...], 'image name']
      * An example is: ['Stardew Valley', '15', '100+', ['Nintendo Switch', 'Playstation', 'Xbox', 'PC', 'Mobile'], 'stardew.jpg']

## UML Diagram
<img width="507" alt="Screenshot 2024-02-26 at 4 08 12 PM" src="https://github.com/paullim2/cs361_vg_recommender_ms/assets/129928704/8cedd3a1-8d70-4e6a-acf0-91981edf14f9">
