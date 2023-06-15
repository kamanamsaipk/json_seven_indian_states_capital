#Assignment-1 part2
import json
data = {
    "Gujarat":"Gandhinagar",
    "Maharasthra":"Mumbai",
    "Karnataka":"Bangalore",
    "Tamilnadu":"chennai",
    "Uttar pradesh":"Lucknow",
    "Kerala": "Thiruvananthapuram",
    "punjab":"chandigarh"
}
with open('indian_states.json','w') as f:
    json.dump(data,f)
    

