__author__ = 'Mohammad ali'

from tokenize import Tokenize
from process import Process

def main():
        p=Process()
        print(p.proces('5+6-(2*6-3)/3'))
        print(p.proces('12+2*6-(15/3*2)-7'))
        print(p.proces('5/1-5+2*(7+2/2*7)-4/2'))
        print(p.proces('(8/2*6)-4+(14*2)-50'))
        return



if __name__ == '__main__':
    main()