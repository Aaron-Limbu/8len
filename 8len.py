import argparse
import sys

MAX = int(636)
def prompt_user_input():
    uinput=''
    while True:
        uinput = input('enter file name').strip()
        name = uinput.split('.')
        if(name[1].lower() == 'txt'):
            break
        else:
            print('enter proper file name')
    return uinput 

strings = []
nstrings = []
def read_file(input_str,args):
    with open(input_str,"r",encoding = "ISO-8859-1") as rfile:
        for line in rfile:
            if(len(line) > 7):
                if(len(strings)>MAX):
                    nstrings.append(strings)
                    strings.clear()

                else:
                    strings.append(line)
                               

def main():
    parser = argparse.ArgumentParser(description="creates file that contains words greater than 7")
    parser.add_argument('-i','--input',type=str,help='Input the file, example a.txt')
    parser.add_argument('-o','--output',type=str,help='Out put file name')
    args = parser.parse_args()
    if args.input:
        input_str = args.input
        read_file(input_str,args)
    else:
        input_str = prompt_user_input()
        read_file(input_str,args)
    if args.output:
        with open(args.output,'w') as ofile:
            for string in nstrings:
                for i in string:
                    ofile.write(f'{i}')
    else: 
         for string in nstrings:
                for i in string:
                    i = i.split('\n')
                    print(i[0])   

main()
