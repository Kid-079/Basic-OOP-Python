from Food import FoodSeafood, FoodTraditionalFood

costumer1 = FoodSeafood('Udang Extra Pedas')
costumer2 = FoodTraditionalFood('Rawon Asam Pedas')

costumer1.show_info()
costumer2.show_info()

costumer1.gainExp = 300
costumer2.gainExp = 400
costumer1.show_info()
costumer2.show_info()
