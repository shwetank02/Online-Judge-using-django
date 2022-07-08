import os, filecmp

def check_code(sub):
    file=open(r'S:\study\online_judge\judge\out.cpp', 'w+')
    file.write(sub.code)
    file.close()
    # if(not os.system('g++ S:\study\online_judge\judge\out.cpp')):
    #     verdict = "Compilation Error"
    # else:
    #     os.system('a,out <S:\study\online_judge\judge\TESTinput.txt> S:\study\online_judge\judge\output.txt')
    #     out1='S:\study\online_judge\judge\output.txt'
    #     out2='S:\study\online_judge\judge\TESToutput.txt'
    #     if(filecmp.cmp(out1,out2,shallow=False)):
    #         verdict='Accepted'
    #     else:
    #         verdict='WA'
    # sub.verdict=verdict
    # sub.save()
    # with open('out.cpp', 'wb+') as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)
    #open('out.cpp', 'w+')
    z=os.system("g++ S:\study\online_judge\judge\out.cpp -o S:\study\online_judge\judge\out.exe")
    if(z==0):
        if(os.system("timeout --preserve-status 1 .\out.exe < .\TESTinput1.txt > .\output.txt")!=0):
        #if os.system("timeout --preserve-status 1 S:\study\online_judge\judge\out < TESTinput.txt > output.txt") != 0:
            verdict="TLE"
        else:
            out1='S:\study\online_judge\judge\output.txt'
            out2='S:\study\online_judge\judge\TESToutput.txt'
            if(filecmp.cmp(out1,out2,shallow=False)):
                verdict='Accepted'
            else:
                verdict='WA'
    else:
        verdict="CE"
    print(verdict)
