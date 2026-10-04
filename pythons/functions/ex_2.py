def chai_orders():
    chai_type = "Ginger"

    def new_order():
        chai_type = "Elachi"
        print("Inner ", chai_type)
    new_order()

    print("outer ", chai_type)    


chai_type = "Masala"
chai_orders()
print("Global ", chai_type)    