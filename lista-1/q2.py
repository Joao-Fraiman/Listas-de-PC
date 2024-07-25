import math

x = float(input('x? '))
y = float(input('y? '))
z = float(input('z? '))


result_1 = (x**2 + y**2 + z**2)**(1/3)
print(f'({x}^2 + {y}^2 + {z}^2)^(1/3) = {result_1}')

result_2 = x**y + y**z
print(f'{x}^{y} + {y}^{z} = {result_2}')

result_3 = math.cos(x**2 + y**2) + math.sin(y**2 + z**2)
print(f'cos({x}^2 + {y}^2) + sin({y}^2 + {z}^2) = {result_3}')

result_4 = (math.log10(x) + math.log10(y) + math.log10(z))**(x + y + z)
print(f'(log({x}) + log({y}) + log({z}))^({x} + {y} + {z}) = {result_4}')
