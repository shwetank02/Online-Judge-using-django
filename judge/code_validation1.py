from .models import testcase
import os, filecmp, sys, subprocess

def check_code(submission):
    with open("S:\study\online_judge\judge\Testcases\question1\sol.cpp", "w") as f:
        f.write(submission.code)
    f.close()
    if sys.platform == 'linux':
        command =['g++ sol.cpp']
    else:
        path_to_code = r"S:\study\online_judge\judge\Testcases\question1"
        command = 'g++ ' + os.path.join(path_to_code, 'sol.cpp')

    # Try code compilation
    try:
        subprocess.run(command, capture_output = True, check = True)
    except subprocess.CalledProcessError:
        print("Compilation Error")
        submission.verdict = "Compilation Error"
        submission.save()
        return
    if sys.platform == 'linux':
        command = ['./a.out']
    else:
        command = ['a.exe']

    z=testcase.objects.get(curr_problem=submission.curr_problem)
    input=z.input
    output=z.output
    input=input.split(',')
    output1=output.split(',')
    n=len(input)
    for i in range(n):
        testinput=input[i]
        testoutput=output1[i]
        f = open(testinput, 'r')
        f_content= f.read()
        try:
            output = subprocess.run(command, capture_output = True, \
                    text = True, input = f_content, check = True, timeout = 2)
        except subprocess.TimeoutExpired:
            submission.verdict = "TLE"
            submission.save()
            return
        f.close()
        out1="S:\study\online_judge\judge\Testcases\question1\output.txt"
        with open(out1, "w") as f:
            f.write(output.stdout)
        f.close()

         #Calculate the verdict and save it
        if(filecmp.cmp(out1,testoutput,shallow=False)):
            submission.verdict='Accepted'
            submission.save()
        else:
            submission.verdict='WA'
            submission.save()
            return


