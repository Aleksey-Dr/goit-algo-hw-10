from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem(name="maximize_drinks_production", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total products"

model += (2 * lemonade + 1 * fruit_juice <= 100), "Water constraint"
model += (1 * lemonade <= 50), "Sugar constraint"
model += (1 * lemonade <= 30), "Lemon juice constraint"
model += (2 * fruit_juice <= 40), "Fruit puree constraint"

status = model.solve()

print(f"Resolution status: {status}")
print(f"Maximum amount of Lemonade: {value(lemonade)}")
print(f"Maximum amount of Fruit Juice: {value(fruit_juice)}")
print(f"Total number of products: {value(lemonade + fruit_juice)}")