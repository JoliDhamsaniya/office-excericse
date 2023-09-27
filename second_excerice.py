# Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
# •Add a new member function to generate “display_name”.
# •“display_name” has the text value as below.
# 1.Vehicle category without parent then “Vehicle” 
# 2.Car category with “Vehicle” as a parent then “Vehicle > Car”
# 3Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
# •Create 5 category objects with parent and child relation.
# •Create 3 product objects in each category.
# •Display the Category with its Code, Display Name, and all product details inside that category.
# •Display product list by category ( group by category, order by category name).




class category:
    def __init__(self,name,code,parent=None):
        self.name = name
        self.code = code
        # self.no_of_products = 0
        self.parent = parent
        self.display_name = self.g_display_name()
        self.products =[]


    def __str__(self):
        return f"category:{self.name} \n code:{self.code}"

# Add a new member function to generate “display_name”.
    def g_display_name(self):
        if self.parent:
            return f"{self.parent.display_name} > {self.code}"
        else:
            return self.code

    def list_appned():
        for details in products:
            products.append(category)


    def display():
        categories = [vehicle,car,petrol]
        for category in categories:
            print(f"category code:{category.code}")
            print(f"display name:{category.display_name}\n")
            for product in category.products:
                print(f"products name:{product.name}")
                print(f"product code:{product.code}\n")
                print(f"product category:{product.category}\n")



class product:
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.category=category
        self.price=price

    def __str__(self):
        return f"category:{self.name} \n code:{self.code}\n category:{self.category} \n price:{self.price}"



# Vehicle category without parent then “Vehicle” 
vehicle = category("vehicle",1,parent=None)
# Car category with “Vehicle” as a parent then “Vehicle > Car”
car = category("car",2,parent=vehicle)
# Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
petrol = category("petrol",3,parent=car)
plan = category("plan",4,parent=petrol)
food = category("food",5,parent=plan)
mobile = category("mobile",6,parent=food)




products=[
product("apple",120,vehicle,1000000),
product("redmi 9 prime",121,vehicle,20000),
product("vivo",123,vehicle,15000),
product("bmw",501,car,50000000),
product("XQV",502,car,1000000),
product("i20",503,car,7000000),
product("kitkat",123,petrol,10),
product("5star",124,petrol,5),
product("park",125,petrol,10),
product("dariy milk",126,petrol,50)
]

# print object
print("category info with its no_of_products")
print(vehicle,"\n")
print(car,"\n")
print(petrol,"\n")

# Display the Category with its Code, Display Name, and all product details inside that category.

categories =[vehicle,car,petrol,plan,mobile]
for p in products:
    p.category.products.append(p)


# Display product list by category ( group by category, order by category name).
print("display_name")
category.display()
category.list_appned()



