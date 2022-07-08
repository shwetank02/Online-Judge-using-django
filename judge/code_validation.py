import os, filecmp
from .models import testcase

def check_code(sub):
    file=open(r'S:\study\online_judge\judge\Testcases\question1\out.cpp', 'w+')
    file.write(sub.code)
    file.close()
    z=testcase.objects.get(curr_problem=sub.curr_problem)
    input=z.input
    output=z.output
    input=input.split(',')
    output=output.split(',')
    n=len(input)
    "S:\study\online_judge\judge\Testcases\question1\TESTinput1.txt"
    if(os.system('g++ S:\study\online_judge\judge\Testcases\question1\out.cpp')!=0):
        verdict='Compilation Error'
        sub.verdict=verdict
        sub.save()
        return
    for i in range(n):
        testinput=input[i]
        testoutput=output[i]
        z='a,out <' + str(testinput) + '> S:\study\online_judge\judge\Testcases\question1\output.txt'
        os.system(z)
        out1='S:\study\online_judge\judge\Testcases\question1\output.txt'
        if(filecmp.cmp(out1,testoutput,shallow=False)):
            verdict='Accepted'
        else:
            verdict='WA'
            break

    sub.verdict=verdict
    sub.save()
    return
    # with open('out.cpp', 'wb+') as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)
    #open('out.cpp', 'w+')
    # if os.system("g++ out.cpp -o out") == 0:
    #     if os.system("timeout --preserve-status 1 ./out < TESTinput.txt > output.txt") != 0:
    #         print("TLE")
    #     else:
    #         if os.system("diff output.txt TESToutput.txt") == 0:
    #             print("AC")
    #         else:
    #             print("WA")
    # else:
    #     print("CE")
