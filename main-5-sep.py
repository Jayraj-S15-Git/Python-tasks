class Earphones:
    def _init_(self, Company, Price, Color, BL):
        self.company = Company
        self.price = Price
        self.color = Color
        self.battery_life = BL

    def PrintInvoice(self):
        print("Company :", self.company)
        print("Colour :", self.color)
        print("Battery Life :", self.battery_life)
        print("Price :", self.price)

# Create instances
ap1 = Earphones("Apple", 25000, "White", 3)
ap1.PrintInvoice()
ap2 = Earphones("Boat", 15000, "Black", 4)
ap2.PrintInvoice()
ap3 = Earphones("Boat", 15000, "Black", 4)
ap3.PrintInvoice()
ap4 = Earphones("Boat", 15000, "Black", 4)
ap4.PrintInvoice()
