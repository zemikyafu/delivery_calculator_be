## Python Flask API for Delivery fee calculator

The POST endpoint accepts parameters such as cart_value, delivery_distance, number_of_items, and time. The service calculates the delivery fee based on the information provided in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

### Rules for calculating a delivery fee
1) If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€.
2) A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
3) If the number of items is five or more, an additional 50 cent surcharge is added for each item above and including the fifth item. An extra "bulk" fee applies for more than 12 items of 1,20€
4) During the Friday rush, 3 - 7 PM, the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x.
5) The delivery fee can never be more than 15€ and The delivery is free (0€) when the cart value is equal or more than 200€.

