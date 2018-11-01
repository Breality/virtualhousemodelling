# virtualhousemodelling
188 models to decorate your house. Love the design? We email you the retail prices and purchase link for all items!
# What it does
Using voice activated commands, you can place/rotate/cancel/move/destroy items in your virtual house. You see the models up close in Virtual reality, moving your position with the xbox controller. Most importantly, you can interact with our AI in a normal conversation, and it will load models for you to place as soon as one of the words you say has a search result. Don't have enough time? Just say "Save" to save current house. Yes, it will load. Can't get enough of it? Just say "Email" at any time so that we can email you the list of items you have, the retail price for each, and a link to purchase it. We even total it up for you in case you want to go on a shopping spree!

# How we built it
Our client was made in Unity. In order to load the models, we used WayFair's API which provided us with an endpoint to the 188 models. Unfortunately, we couldn't get google's voice recognition API installed on Unity so we had to set it up with window's voice recognition. We used google cloud to store our data, and set up an end point in c# for our clients to ping so that we can put the data securely.

# Challenges we ran into
A very challenging part was planning and creating an efficient system that does what we want it to do. We had to make a program that loads hundreds of models, listens to speech, runs VR, renders HD graphics, and sends requests frequently. Overall, we did a good job on keeping the program efficient.

# What's next for Virtual House Modeling
This can be expanded to use more than just one store API, it can compare prices from multiple retailers while allowing you to see the differences in virtual reality in an environment like your house. The project has lots of potential, though no one knows where it will go just yet.
