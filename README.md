# Setup
1. Download 'vg_recommender_microservice.py' and store in the same folder of your HTML file.
2. Install Flask from your Python library.
3. Open the microservice file, and under 'def index()', change HTML string to be equal to your HTML file name. Save.
4. Run 'vg_recommender_microservice.py'.

# Communication Contract
## Requesting Data from the Microservice
1. In your HTML file in the form box(es) to select videogame preferences, add the following:
   action="submit" method="post"

## Receiving Data from the Microservice
1. A valid response looks like: ['Stardew Valley', '15', '100+', ['Nintendo Switch', 'Playstation', 'Xbox', 'PC', 'Mobile'], 'stardew.jpg']
