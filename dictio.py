city= {"satyam":"new delhi",
       "sam":"mumbai",
       "jetaan":"chandigarh"
       }
print(city, type(city))
print(city.items())
print(city.keys())
print(city.values())
city.update({"satyam":"pune"})
print(city)
print(city.get("satyam"))