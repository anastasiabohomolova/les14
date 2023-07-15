class One:
    def __init__(self, *args, **kwargs):
        self.args = args

    def method(self):
        return self.args

    def func_dodatok(self):
        return(self.args + self.args)


class Two:
    def __init__(self, *args, **kwargs):
        self.args = args

    def method(self):
        return self.args

    def func_dodatok(self):
        return(self.args + self.args)

class Three:
    def __init__(self, *args, **kwargs):
        self.args = args
    def method(self):
        return self.args

class Four:
    def __init__(self, *args, **kwargs):
        self.args = args

    def m(self):
        return self.args


obj_one = One(1, 'one', 3434343)
obj_two = Two(2, 'two')
obj_three = Three(3, 'three')
obj_four = Four(4, 'four')

lst_objs = [obj_one, obj_two, obj_three, obj_four]
def my_func():
    lst_objs_new = []
    for i in lst_objs:
        if isinstance(i, One):
            dict_method_one = dict.fromkeys([obj_one], obj_one.method())
            lst_objs_new.append(dict_method_one)
        elif isinstance(i, Two):
            dict_method_two = dict.fromkeys([obj_two], obj_two.method())
            lst_objs_new.append(dict_method_two)
        elif isinstance(i, Three):
            dict_method_three = dict.fromkeys([obj_three], obj_three.method())
            lst_objs_new.append(dict_method_three)

    d = {}
    for el in lst_objs_new:
        d.update(el)

    return d


f = my_func()
print(f)

def my_func_2():
    lst_for_func_dodatok = []
    for i in lst_objs:
        if isinstance(i, One):
            dict_func_2_one = dict.fromkeys([obj_one], obj_one.func_dodatok())
            lst_for_func_dodatok.append(dict_func_2_one)
        elif isinstance(i, Two):
            dict_func_2_two = dict.fromkeys([obj_two], obj_two.func_dodatok())
            lst_for_func_dodatok.append(dict_func_2_two)

    d_2 = {}
    for el in lst_for_func_dodatok:
        d_2.update(el)

    return d_2

ff = my_func_2()
print(ff)
