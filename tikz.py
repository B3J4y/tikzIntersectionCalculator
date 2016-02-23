import sys, ast, getopt, types, pyperclip
import numpy as np
from fractions import Fraction

def main(argv):            
    plane = {}
    lines = []
    if len(argv) > 0:
        plane, lines = interpreteArgs(argv)
    else :
        print "No arguments"
        print "Insert the data manually"
        geomObjs = {"plane":[],
                "lines":[]}
        coords = 3
        for obj in ["plane", "lines"] :
            myobj = interact(coords, obj);
            geomObjs[obj].append(myobj);
            coords = coords - 1
        print geomObjs 
        print "Do you want to add further lines?"
        isGood = 0
        coords = 2;
        while not isGood:
            t = raw_input("Enter nothing if u want to stop adding new lines: ")
            if len(t) == 0:
                isGood = 1
                continue;
            
            geomObjs["lines"].append(interact(2, "lines"))
        plane = geomObjs["plane"][0]
        lines = geomObjs["lines"]


    res = "";
    iteration = 0
    print plane, lines
    for line in lines :
        
        if len(res) > 0:
            res += "\n"
        res += intersectPlaneLine(plane, line, iteration);
        iteration = iteration + 1;
    print res
    pyperclip.copy(res)
    print "saved in your clipboard"

def interact(coords, obj):
    returnObj = {}
    for x in range(0,coords):
        isGood = 0
        while not isGood:
            print "Give me the " + str(x) + ". value for the " + obj
            t = raw_input("Input the points looks like 0,0,0: ")
            try:
                newVal = map(float, t.split(","))
                test = np.array(newVal)
            except:
                print "Something went wrong"
                continue;
            if not test.shape[0] == 3 :
                print "We need 3 Dimensions"
                continue;
            returnObj[x] = newVal
            isGood = 1
    return returnObj



def interpreteArgs(argv) :
    arg_dict={}
    switches={'plane':dict, 'line':dict, 'opt':dict}
    singles=''.join([x[0]+':' for x in switches])
    long_form=[x+'=' for x in switches]
    d={x[0]+':':'--'+x for x in switches}
    plane = {}
    lines = []
    try:            
        opts, args = getopt.getopt(argv, singles, long_form)
    except getopt.GetoptError:          
        print argv
        print singles
        print long_form
        print "bad arg"                       
        sys.exit(2)       

    for opt, arg in opts:        
        if opt[1]+':' in d: o=d[opt[1]+':'][2:]
        elif opt in d.values(): o=opt[2:]
        else: o =''
        if o and arg:
            try:
                arg_dict[o]=ast.literal_eval(arg)
            except:
                print "Mal formed string, man"
                if o == "plane":
                    print "try: {0:[0,0,0], 1:[1,1,0], 2:[1,1,1], 3:[0,0,1]}"
                elif o == "line":
                    print "try: {0:[0,0,0], 1:[1,1,1]}"
                elif o == "opt":
                    print "try: {0:[0,0,0], 1:[1,1,1]}"
                return

        if not o or not isinstance(arg_dict[o], switches[o]):    
            print opt, arg, " Error: bad arg"
            sys.exit(2)                 
    for e in arg_dict:
        if e == "plane":
            plane = arg_dict[e];
        if e == "line":
            lines.append( arg_dict[e]);
        if e == "opt":
            lines.append( arg_dict[e]);
    return plane, lines;

def intersectPlaneLine(plane, line, i) :
    p0 = np.array(plane[0])
    u = p0 - np.array(plane[1])
    v = p0 - np.array(plane[2])
    u = u / np.linalg.norm(u)
    v = v / np.linalg.norm(v)
    n = np.cross(u, v)
    n = n / np.linalg.norm(n)
    l0 = np.array(line[0])
    ld = np.array(line[1]) - l0

    unknown = np.sum(n * ld)
    known = np.sum(n * (p0 - l0))

    point = known / unknown * ld + l0
    point = np.round(point, 2)
    print "n, l0, ld, unknown, known, point"
    print n, l0, ld, unknown, known, point
    return "\coordinate (T" + str(i) + ") at (" + point[0].astype("str") + "," + point[1].astype("str") + "," + point[2].astype("str") + ");"

if __name__ == '__main__':
    main(sys.argv[1:])  
