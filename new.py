class category:
    def __init__(self,name,code):
        self.name = name
        self.code=code
        self.no_of_products=0

    def __str__(self):
        return f"category:{self.name} \n code:{self.code}\n no_of_product:{self.no_of_products}"

class product:
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.category=category
        self.price=price


    def __str__(self):
        return f"product:{self.name}\n code:{self.code}\n category:{self.category}\n price:{self.price}"

object1 = category("mobile",111)
object2 = category("car",500)
object3 = category("chocolates",200)


product1 = product("apple",120,"object1",1000000)
product2= product("redmi 9 prime",121,"object1",20000)
product3 = product("vivo",123,"object1",15000)
product4 = product("bmw",501,"object2",50000000)
product5 = product("XQV",502,"objcet2",1000000)
product6 = product("i20",503,"object2",7000000)
product7 = product("kitkat",123,"object3",10)
product8 = product("5star",124,"object3",5)
product9 = product("park",125,"object3",10)
product10 = product("dariy milk",126,"object3",50)

products = [product1,product2,product3,product4,product5,product6,product6,product7,product8,product9,product10]

object1.no_of_products=3
object2.no_of_products =3
object3.no_of_products=4

# for product in products:
#     product.category.no_of_products += 1




print(object1,"\n")
print(object2,"\n")
print(object3,"\n")


print("print products:")
sort_products = sorted(products,key=lambda x: x.price, reverse=True)
for products in sort_products:
    print(products ,"\n")

searchproduct = int(input("enter the code:"))
found_product = next((product for product in products if product.code == searchproduct), None)
if found_product:
    print(f"\nProduct Found: {found_product}")
else:
    print(f"\nProduct with code '{searchproduct}' not found.")
