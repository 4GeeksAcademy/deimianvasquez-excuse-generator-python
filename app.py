import random
who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broked']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']


def generate_excuse(arr):
    num_random = random.choice(arr)
    return num_random



print(generate_excuse(who), generate_excuse(what), generate_excuse(when))