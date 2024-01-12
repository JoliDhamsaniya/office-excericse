# Create a new class named "Customer" with below members. "name","email","phone","street","city","state","country","company","type".
# "type" must be from "company,contact,billing,shipping".
# "Company" must be a Customer object which is the parent object.
# Apply Multiple possible validation for phone number and email
# Does not allowed number in name,city,state and country
# Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
# "company", "billing", "shipping" are objects of Customer.
# "date" must be today or the future. Does not allow past date.
# "total_amount" auto calculated based on different products inside order.
# "order_lines" is list of objects of "OrderLine"
# create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
# "order" is the object of Order.
# "subtotal" is auto calculated based on quantity and price.
# Display Order and Customer Information
# Sort orders based on "date".
# User can filter the current
# month orders
# Search Orders from its number.
# List/Display all orders of a specific product



import re
from datetime import date, datetime

# Create a new class named "Customer" with below members. "name","email","phone",
# "street","city","state","country","company","type".
class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, cust_type):
        self.name = self.validate_items(name)
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.street = street
        self.city = self.validate_items(city)
        self.state = self.validate_items(state)
        self.country = self.validate_items(country)
        self.company = company
        self.type = self.validate_cust_type(cust_type)

# Apply Multiple possible validation for phone number and email
    def validate_email(self,email):
        if re.match(r"[^@]+@[^@]+\.[^@]+",email):
            return email
        else:
            print("email is not match")
    def validate_phone(self,phone):
        if re.match(r"^\+?\d{8,15}$",phone):
            return phone
        else:
            print("phone not match")
    def validate_items(self, name):
        if re.match(r"^[^0-9]+$",name):
            return name
    def validate_cust_type(self,cust_type):
        type = ['company','contact','biling','shipping']
        if cust_type in type:
            return cust_type

# Create a new class named "Order" with members "number","date", "company", "billing",
# "shipping", "total_amount","order_lines".
class Order:
    def __init__(self, number, date1, company, billing, shipping):
        self.number = number
        self.date1 = self.validate_date(date1)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.total_amount = 0
        self.order_lines = []

# date" must be today or the future. Does not allow past date
    def validate_date(self,date1):
        td = datetime.strptime(date1, '%d-%m-%Y').date()
        today = date.today()
        if td < today:
            print("date is not valid fromat")
        else:
            return date1
    def add_orderline(self,order_line):
        self.order_lines.append(order_line)
        self.total_amount =self.total_amount + order_line.subtotal

    def display_order_lines(self):
        print(f" order Number: {self.number}")
        print(" order Lines:")
        for  line in (self.order_lines):
            print( f"  Product: {line.product}, Quantity: {line.quantity}, Price: {line.price}, Subtotal: {line.subtotal}")


    def order_info():
        print()
        for y in order:
            print(f" order number:{y.number}")
            print(f" order date:{y.date1}")
            print(f" order company:{y.company}")
            print(f" order billing:{y.billing}")
            print(f" order name:{y.shipping}")
            print(f" order line:{y.display_order_lines()}")
            print()


# create a new class named "OrderLine" with members "order", "product", "quantity", "price",
#
class orderline:
    def __init__(self,Order,product,quantity,price):
        self.order = Order
        self.product = product
        self.quantity = quantity
        self.price = price
    # "subtotal" is auto calculated based on quantity and price.
        self.subtotal = quantity * price

customer1 = Customer("amul","jolla@gmmail.com","123456789","abc","rajkot","gujrat","india",None,cust_type="company")
customer2 = Customer("lekme","hmg@gmail.com","9112345678","cde","rajkot","gujarat","india",customer1,cust_type="shipping")
customer3 = Customer("zara","jhk@gmail.com","9714551478","qwe","jamanagar","gujrat","india",customer1,cust_type="billing")
customer4 = Customer("boat","bot@gmmail.com","1285256789","abc","mumbai","maharast","india",None,cust_type="company")
customer5 = Customer("apple","pple@gmail.com","9112345678","cde","rajkot","gujarat","india",customer4,cust_type="shipping")
customer6 = Customer("lenskart","lenskart@gmail.com","9714551478","qwe","jamanagar","gujrat","india",customer4,cust_type="billing")
C = [customer1,customer2,customer3,customer4,customer5,customer6]

order1 = Order("1", "15-7-2024", "customer1", "zara", "lekme")
order2 = Order("2","20-6-2024","customer4","lenkart","apple")
order3 = Order("3","15-1-2024","customer1","zara","lekme")
order4 = Order("4","18-1-2024","customer1","qwe","rty")
order = [order1,order2,order3,order4]

# order_lines" is list of objects of "OrderLine"
orderline1  = orderline(order1,"ice cream",1,200)
orderline2 = orderline(order2,"foundation",15,100)
orderline3 = orderline(order3,"shirt",20,400)
orderlines = [orderline1,orderline2,orderline3]

for i in order:
    for j in orderlines:
        if i.company == j.order.company:
            i.add_orderline(j)



def customer_info():
    print()
    print("customer:")
    for x in C:
        print(f"customer name:{x.name}")
        print(f"customer email:{x.email}")
        print(f"customer phone no:{x.phone}")
        print(f"customer city:{x.city}")
        print(f"customer street:{x.street}")
        print(f"customer state:{x.state}")
        print(f"customer country:{x.country}")
        print()
# customer_info()

# def orderline_info():
#     for z in orderlines:
#         print(f"{z.order}")
#         print(f"{z.product}")
#         print(f"{z.quantity}")
#         print(f"{z.price}")
#         print(f"{z.company}")
#         print()

 # Display Order and Customer Information Sort orders based on "date".
def sort_orders_bydate():
    print("______________________________________________________________Display Order and Sort orders based on date________________________________________________________________________________________________________________")
    n = len(order)
    while n > 0:
        swapped = False
        for i in range(n-1):
            if datetime.strptime(order[i].date1, '%d-%m-%Y').date() > datetime.strptime(order[i + 1].date1,'%d-%m-%Y').date():
                order[i], order[i + 1] = order[i + 1], order[i]
        swapped = True
        if not swapped:
            break
        n -= 1
    print()
    print(f"order Sorted by Date:")
    for orders in order:
        print(f"order date{orders.date1}")
        print(f" order No: {orders.number}")
        print(f"order company{orders.company}")
        print(f"order billing{orders.billing}")
        print(f"order shiping{orders.shipping}")

# User can filter the current  month orders
def sort_orderbymonth():
    print("__________________________________________________________User can filter the current month orders___________________________________________________________________________________________________")
    for i in order:
        current_month = datetime.now().month
        if datetime.strptime(i.date1, '%d-%m-%Y').month == current_month:
            print()
            print("order based on current month:")
            print(f"Order Date: {i.date1}")
            print(
                f"Order No: {i.number} \nOrder Company: {i.company} \nOrder Billing company: {i.billing} \nOrder Shipping company: {i.shipping}\n")

def search_order():
    print("__________________________________________________________________Search Orders from its number____________________________________________________________________________________________________")
    searchorder = input("pelase enter the order number you want to search:")
    for orderno in order:
        if orderno.number == searchorder:
            print(f" product is found")
            print(f" order no:{orderno.number} \n order date:{orderno.date1}\n order company{orderno.company}\n order billing company:{orderno.billing} \n order shipping company:{orderno.shipping}")
        else:
            print(f" product is not found")

# List/Display all orders of a specific product
def display_product():
    print("______________________________________________________________List/Display all orders of a specific product___________________________________________________________________")
    displayproduct = input("please enter product you want to display:")
    for orderproduct in orderlines:
        if orderproduct.product == displayproduct:
            print("product is found")
            print(f"product:{orderproduct.product} \nproduct quantity{orderproduct.quantity}\nproduct price:{orderproduct.price}")
        else:
            print("product is not found")

customer_info()
sort_orders_bydate()
sort_orderbymonth()
search_order()
display_product()
for k in order:
    print("________________________________________________________________________________display orderline based in order__________________________________________________________________")
    k.display_order_lines()







