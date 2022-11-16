# Single Inheritance
class Nokia:
    company = "Nokia Indai"
    website = "www.nokia-india.com"
    
    def contact_details(self):
        print("Address: Cherry Road, Near Bus stand ,salem")

class Nokia1100(Nokia):
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998
    def product_details(self):
        print("Product Name: ",self.name)
        print("Company Name: ",self.company)
        print("Release year: ",self.year)
        print("Website     : ",self.website)

mobile = Nokia1100()
mobile.product_details()
mobile.contact_details()