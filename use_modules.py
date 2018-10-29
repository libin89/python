# for example, have a file module_name.py
# import module_name
# from module_name import function_name
# from module_name import func1,func2
# from module_name import function_name as fn
# import module_name as mn
# from module_name import * (usually, cannot be used)

## NOTE THAT:
#  all the import statement should be placed at the head of file(unless
#  comments at the head).

from function import make_pizza, build_profile
make_pizza(15, 'peperoni')
print(build_profile('tom', 'jeans', age=24))

from function import make_pizza as mp
mp(14, 'green peppers', 'extra cheese')
