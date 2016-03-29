from konig.lextree import Type
import konig.lextree

the = konig.lextree.LexTree(['the'], Type.et_e)
car = konig.lextree.LexTree(['car'], Type.e_t)
flew = konig.lextree.LexTree(['flew'], Type.e_t)


res = the + car
the_car = res[0]

print('the car')
print('===')

print('res  ', res)
print('obj  ', the_car)
print('toks ', the_car.tokens)
print('type ', the_car.type)
print('left ', the_car.left.tokens)
print('right', the_car.right.tokens)
print('rule ', the_car.rule)

res = the_car + flew
the_car_flew = res[0]

print('the car flew')
print('===')

print('res  ', res)
print('obj  ', the_car_flew)
print('toks ', the_car_flew.tokens)
print('type ', the_car_flew.type)
print('left ', the_car_flew.left.tokens)
print('right', the_car_flew.right.tokens)
print('rule ', the_car_flew.rule)
