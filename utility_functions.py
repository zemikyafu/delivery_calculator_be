from datetime import datetime
import pytz

# function to calculate surcharge by distance
def charge_per_distance(delivery_distance):

    base_fee = 200  # Base fee: 2€
    fee_per_500m = 100  # fee per 500m : 1€
    if delivery_distance <= 1000:
            return base_fee
    else:
            additional_distance = delivery_distance - 1000
            if (additional_distance % 500 == 0):
               additional_fee = (additional_distance // 500) * fee_per_500m
            else:
                additional_fee = ((additional_distance // 500) + 1) * fee_per_500m

            return base_fee + additional_fee
    
# function to calculate surcharge based on item number 
def charge_per_number_of_items(number_of_items):
     
    base_surcharge = 50 # 50 cent
   
    bulk_fee = 120 # 1.2 €

    if   4 < number_of_items < 12:
           return  (number_of_items-4) * base_surcharge 
       

    elif number_of_items > 12 :
          return   (number_of_items-4) * base_surcharge + bulk_fee
         
    else:
          return 0;

# check  if the delivery time is at the rush hour 
def is_friday_rush(delivery_time):
  
    delivery_time = datetime.strptime(delivery_time, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.UTC)
    if (delivery_time.weekday() == 4  and 15 <= delivery_time.hour < 19  ):
       return True
      
    else :       
          return False
          