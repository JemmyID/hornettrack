# 🦋 HorneTrack

HornetTrack is a experimental project for auto stalk user on gay dating app Hornet.

- Inspired by [GrindrMap](https://grindrmap.neocities.org/)
- Motivated by [MapleStory BGM- Shattered Time ](https://www.youtube.com/watch?v=h_jJjw1TPyY)

## Concept
Tracking techinque is really simple : trilateration + flood of requests

Hornet blurring method is symmetry in all direction, which makes it easy to exploit an user accurate location with flood of requests.

### Here's how the webpage works:
#### Rought part
It is known that Hornet auto-blur user distance in certain range, and the highest accuracy is 80m. As the result, once you submit user account, sever will trilaterate user to a point in the range of 80m

#### Accurate part
In order to improve accuracy, it makes requests of every small interval from the point you just found in rough part.
After all requests done, take the average of locations in requests which response 80m from Hornet server.


## Future works
🌐 geolocation 

👣⌚ timeline

## Report to Hornet
Hornet do not think the distance information is a fault.
They had discussed to restrict the information shown, but they don't think this is a positive impact.

> The decision to restrict the grid was not taken likely and we have tried to balance this with new features being added.

said Francisco, the hornet customer service.


## Disclaimer 
- Author have no legal liability to user's action.
- Do not abuse this website. The world is filled with love, go outside and explore your new story.