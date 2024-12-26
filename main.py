#!/usr/bin/env python

import random



cities=["New York" , "London" , "Paris" , "Tokyo" , "Berlin" , "Sydney" , "Dubai" , "Moscow" , "Beijing" , "Rome" , "Istanbul" , "Toronto" , "Mumbai" , "Cape Town" , "Kuala Lumpur"]

sales={}



for i in range(45):

    city = random.choice(cities)

    sales[city] = sales.get(city, 0) + random.randint(1000, 5000)



for city, total in sorted(sales.items(), key=lambda x: x[1], reverse=True):

    print(f"{city}: {total}")

