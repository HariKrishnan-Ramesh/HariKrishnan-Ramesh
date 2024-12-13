class Mobile:
    def details(self,company,model,price):
        self.company=company
        self.model=model
        self.price=price

    def display_details(self,company):
        print("Company name is", company)
        print("Model name is ", self.model)
        print("Price is ",self.price)

M=Mobile()
M.details("Motorola","Z2C",20000)
M.display_details("samsung")
