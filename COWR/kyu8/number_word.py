from enum import Enum


class Word(Enum):
    Zero = 0
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9


def switch_it_up(number):
    return Word(number).name

#or
# return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][number]
#or
# return 'Zero One Two Three Four Five Six Seven Eight Nine'.split()[number]
#or
#    number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
#     return number_converter[number]

print(switch_it_up(3))