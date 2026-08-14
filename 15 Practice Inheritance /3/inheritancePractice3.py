from Food import FoodSeafood, FoodTraditionalFood

costumer1 = FoodSeafood('Udang Extra Pedas')
costumer2 = FoodTraditionalFood('Rawon Asam Pedas')

costumer1.show_info()
costumer2.show_info()

costumer1.gainExp = 200
costumer2.gainExp = 300
costumer1.show_info()
costumer2.show_info()
