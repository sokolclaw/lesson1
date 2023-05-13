def get_summ(one, two, delimiter='&'):
    return (str(one) + delimiter + str(two)).upper()
learn_python = get_summ('Learn', 'python')
print(learn_python)
