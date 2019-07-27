from template.tool_kit import timer_deco


@timer_deco
def fast_pow(base, power):
    if power < 0:
        base = 1 / base
        power = -power

    # convert power to binary
    result = 1
    exp = base
    b_power = f'{power:b}'
    for b in reversed(b_power):
        if b == '1':
            result *= exp

        exp **= 2

    return result


@timer_deco
def normal_pow(base, power):
    return base ** power


def main():
    base = 3
    power = 1000000
    a = fast_pow(base, power)
    b = normal_pow(base, power)


if __name__ == '__main__':
    main()
