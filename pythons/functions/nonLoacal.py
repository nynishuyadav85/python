def chai():
    chai_type = "Elachi"

    def change():
        nonlocal chai_type
        chai_type = "Kesar"
    change()
    print(chai_type)    

chai()   