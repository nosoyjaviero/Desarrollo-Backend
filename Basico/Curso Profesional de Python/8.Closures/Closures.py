def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)


print(times10(3)) # 30
print(times4(5)) #20 
print(times10(times4(2))) # 80 

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes repetir cadenas'
        string=string+" "
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola '))


if __name__ == '__main__':
    run()
