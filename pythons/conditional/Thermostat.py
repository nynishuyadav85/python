device_status = input("Device Status " ).lower()

if device_status == "off":
    print("Device is off")
elif device_status == "active":
    temp = int(input("temp "))
    if temp > 35:
        print("Warn: High Temp alert")
    else:
        print("temp normal")
else:
    print("Unknown device status")
