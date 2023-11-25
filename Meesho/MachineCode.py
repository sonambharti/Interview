# Problem statement:


# Develop a program to manage the inventory for an e-commerce company. In this e-commerce website, Admin will create the
# products which will be visible to the customers, The customer can place an order via online payment. Before initiating 
# online payment, we will block the inventory, until it completes the payment.


# Methods to implement:
# 1. create product with given productid, name and inventory count
# createProduct(String productId, String name, Integer count)
 
# 2. return the available quantity for given product
# getinventory(String productid)

# 3. Will be called when the user initiates payment for an order.This will block ordered quantity for the given product and for the given order reference 
# createOrder(List<String> productIds, List<Integer> quantityOrdered, String orderId)
 
# 4. Will be called when the user completes payment for his order. Reduce the ordered quantity permanently for the product corresponding to given orderId.
# confirmOrder(String orderId)


# 5. Will be called when the user cancels payment for his order. The blocked quantity should be released back.
# cancelOrder(String orderId)

# Mandatory use case: 
# All 5 functions should be working and implemented
# Bonus Use case:
# If confirmOrder() is not called within 5min from createOrder(), cancel the order.



# Note: Please focus on the Bonus Feature only after ensuring the required features are complete and demoable. 
# Note: Bonus will be considered only if the required functionality is working.
# Note:ith index of quantityOrdered will be be the quantity of the ith productIds
# Note:An order can have multiple products



# Things to take care of:
# You are free to use the IDE of your choice.
# You can use any library in you code
# You are free to use the language of your choice.
# No External Database(Mysql) is required, you can use in-memory Database, like List, Map etc…
# Do not use any database or NoSQL store, use in-memory store for now.
# Do not create any UI for the application.
# Write a driver class for demo purposes. Which will execute all the commands at one place in the code and test cases.
# The code should be executable (no compiler errors) 
# Demonstration of all the functionalities is important.
# Complete coding within the duration of 60 minutes.
# Use intuitive variable names, function names, class names etc.
# All work should be your own. If found otherwise, you may be disqualified.



# Good to have:
# Modular and clean code.
# Proper naming convention
# Bonus case implementation


    


# HAPPY TEST CASES


# createProduct("ProductId1", "Laptop", 2)


# "ProductId1" -> (Laptop, 2)


# createProduct("2", "Mobile", 5)


# "ProductId2" -> (Mobile, 5)


# createProduct("ProductId3", "Earphone", 4)


# "ProductId3" -> (Earphone, 4)


# getInventory("ProductId1")


# 2


# getInventory("ProductId2")


# 5


# getInventory("ProductId3")


# 4


# createOrder(["ProductId1", "ProductId3"], [1, 2], "OrderId1")


# "ProductId1" -> 1 quantity blocked
# "ProductId3" -> 2 quantity blocked


# confirmOrder("OrderId1")


# "OrderId1" -> (Laptop, 1)


# "OrderId2" -> (ProductId3, 2)
product_details = {}
# product_details[1] = {'name': 'Sonam', 'comp':'Paras'}
# print(product_details[1]['name'])
create_order = {}
# Order_key = {}

class Product():
    
    def __init__(self):
        pass
        # self.productId = productId
        # self.name = name
        # self.count = count
    
    def createProduct(self, productId, name, count):
        self.productId = productId
        self.name = name
        self.count = count
        product_details[productId] = {'name': name, 'count': count}
        print("Product is added succesfully with prod id: ", productId)
        return product_details
        
    def getInventory(self, productId):
        if (self.productId in product_details.keys()):
            count = self.product_details[productId]['count']
            return count
            
class Order(Product):
    # def __init__(self, orderId, productId, quantityOrdered, confirm=False):
    #     self.productId = productId
    #     self.orderId = orderId
    #     self.quantityOrdered = quantityOrdered
    #     if confirm:
    #         self.confirm = True
    
    def createOrder(self, orderId, productId, quantityOrdered, confirm=False):
        # Order_key[orderId] = productId
        total_count = product_details[productId]['count']
        create_order[orderId] = {'Prod Id': productId, 'Quantity ordered': quantityOrdered}
        remain_count = total_count - quantityOrdered
        product_details[productId]['count'] = remain_count
        print("Order Created ....")
        print("Remain count: ", remain_count)
        
    def confirmOrder(self, confirm):
        if confirm:
            print("Order confirm sucessfully...")
        
    def cancelOrder(self, order_id):
        productId = create_order[order_id]['Prod Id']
        quantityOrdered = create_order[order_id]['Quantity ordered']
        remain_count = product_details[productId]['count'] + quantityOrdered
        product_details[productId]['count'] = remain_count
        
        print("Order Canceled ....")
        print("Total amount: ", remain_count)
        
Admin = Product()
addProd = Admin.createProduct('p12', 'speaker', 12)
User = Order()
cOrder = User.createOrder('oid1', 'p12', 2, False)
confOrdef = User.confirmOrder(True)
# cancelOrder = User.cancelOrder('oid1')
    
        
