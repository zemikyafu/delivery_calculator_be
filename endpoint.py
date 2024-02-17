from flask import Flask,request
from datetime import datetime
import utility_functions 


app =Flask(__name__)

#end point for calcuate delivery fee post request 
@app.route("/api/calculate_delivery_fee", methods=["POST"])
def calculate_delivery_fee():
    
    # received post request JSON data
    data = request.get_json()
    cart_value = data['cart_value']
    delivery_distance = data['delivery_distance'] # delivery_distance
    number_of_items = data['number_of_items']
    time =  data['time']
    
  
    rush_rate=1.2
    delivery_fee=0
    response = {"delivery_fee": delivery_fee}
   
    # if the cart value is equal or more than 200 € The delivery is free (0€) 
    if cart_value >= 20000 :
       return response
    else:
         
       distance_charge = utility_functions.charge_per_distance(delivery_distance)
       item_number_charge = utility_functions.charge_per_number_of_items(number_of_items)
       delivery_fee = distance_charge + item_number_charge
       if utility_functions.is_friday_rush(time):
            delivery_fee = delivery_fee * rush_rate # If it is rush hour delivery fee multiplied by the rush rate (1.2)

       delivery_fee = min(delivery_fee, 1500) # Maximum delivery fee can never be more than 15€
       response['delivery_fee'] = delivery_fee
       return response



          


