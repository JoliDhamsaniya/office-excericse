class category:
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def __str__(self):
        return f"category:{self.name} \n code:{self.code}\n no_of_product:{self.no_of_products}"

class product:
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.category=category
        self.price=price

        category.no_of_products += 1
    def __str__(self):
        return f"category:{self.name} \n code:{self.code}\n category:{self.category} \n price:{self.price}"

    def sorthightolowprice():
        n = len(products)
        while n > 0:
            swapped = False
            for i in range(n - 1):
                if products[i].price < products[i + 1].price:
                    products[i], products[i + 1] = products[i + 1], products[i]
                    swapped = True
            if not swapped:
                break
            n -= 1
        for product in products:
            print(product, "\n")

    def sortlowtohighprice():
        n = len(products)
        while n > 0:
            swapped = False
            for i in range(n - 1):
                if products[i].price > products[i + 1].price:
                    products[i], products[i + 1] = products[i + 1], products[i]
                    swapped = True
            if not swapped:
                break
            n -= 1
        for product in products:
            print(product, "\n")

    def searchcode(sccode):
        for product in products:
            if product.code == sccode:
                print(f" product is found:{product}")
                break
        else:
            print(f" product is not found")



object1 = category("mobile",111)
object2 = category("car",500)
object3 = category("chocolates",200)


products=[
product("apple",120,object1,1000000),
product("redmi 9 prime",121,object1,20000),
product("vivo",123,object1,15000),
product("bmw",501,object2,50000000),
product("XQV",502,object2,1000000),
product("i20",503,object2,7000000),
product("kitkat",123,object3,10),
product("5star",124,object3,5),
product("park",125,object3,10),
product("dariy milk",126,object3,50)
]

# print object
print("category info with its no_of_products")
print(object1,"\n")
print(object2,"\n")
print(object3,"\n")

print("high to low")
product.sorthightolowprice()

print("price low to high")

product.sortlowtohighprice()

product.searchcode(126)
