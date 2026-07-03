# Car Store Project

# نسبة الضريبة
TAX_RATE = 0.15

# قائمة السيارات وأسعارها
cars = ["Audi A4", "Audi A6", "Audi Q3", "Audi Q5", "Audi Q7"]
prices = [150000, 220000, 170000, 210000, 280000]

# قائمة لتخزين الطلبات
orders = []

# متغير الاختيار في القائمة
choice = 0

# حلقة تكرار للقائمة الرئيسية
while choice != 4:
    print("\nCar Store Menu")
    print("1. Show cars")     # عرض السيارات
    print("2. Buy car")       # شراء سيارة
    print("3. Show orders")   # عرض الطلبات
    print("4. Exit")          # خروج

    try:
        # أخذ اختيار المستخدم
        choice = int(input("Enter your choice: "))

        # خيار عرض السيارات
        if choice == 1:
            for i in range(len(cars)):
                print(i + 1, cars[i], prices[i], "SAR")

        # خيار شراء سيارة
        elif choice == 2:
            # عرض السيارات أولاً
            for i in range(len(cars)):
                print(i + 1, cars[i], prices[i], "SAR")

            # اختيار السيارة والكمية
            car_number = int(input("Choose car number: "))
            quantity = int(input("Enter quantity: "))

            # التحقق من صحة الإدخال
            if car_number >= 1 and car_number <= len(cars) and quantity > 0:
                car_name = cars[car_number - 1]
                car_price = prices[car_number - 1]

                # حساب السعر
                subtotal = car_price * quantity
                tax = subtotal * TAX_RATE
                total = subtotal + tax

                # حفظ الطلب
                orders.append(total)

                # عرض تفاصيل الطلب
                print("Car:", car_name)
                print("Price:", car_price)
                print("Quantity:", quantity)
                print("Subtotal:", subtotal)
                print("Tax:", tax)
                print("Total:", total)

            else:
                print("Invalid input")

        # خيار عرض الطلبات
        elif choice == 3:
            if len(orders) == 0:
                print("No orders")
            else:
                for i in range(len(orders)):
                    print("Order", i + 1, "=", orders[i], "SAR")

        # خيار الخروج
        elif choice == 4:
            print("Goodbye")

        # إذا المستخدم دخل رقم غير موجود
        else:
            print("Invalid choice")

    # معالجة الخطأ إذا المستخدم دخل شيء غير رقم
    except ValueError:
        print("Please enter numbers only")