import os, argparse, sys

def findReplace(text):
    global args
    best = ""
    bestScore = 0
    for length in range(2, 30):
        if args.status:
            print(".", end="")
            sys.stdout.flush()
        for pos in range(len(text) - length):
            seg = text[pos : pos + length]
            count = text.count(seg)
            score = length * (count - 1)

            if score > bestScore:
                best = seg
                bestScore = score
    return best

def findReplaceChar(text):
    for c in range(32, 127):
        ch = chr(c)
        if ch in "\"'\\":
            continue
        if ch not in text:
            return ch
    return None

def quote(text):
    if not "\n" in text:
        if not "'" in text:
            return "'" + text + "'"
        if not "\"" in text:
            return "\"" + text + "'"
    if not '"' in text:
        return '"""' + text + '"""'
    if not "'" in text:
        return "'''" + text + "'''"
    return repr(text)

def method_int(x):
    x = int(x)
    if not 0 <= x <= 2:
        raise argparse.ArgumentTypeError("Method must be between 0 and 2")
    return x

parser = argparse.ArgumentParser(description="Make a short, obfuscated Python program, printing a specific string")
parser.add_argument("-o", "--output", metavar="PATH", nargs=1, type=str, help="The output destination for the resulting program. If not specified, output goes to STDOUT")
parser.add_argument("-i", "--input", metavar="PATH", nargs=1, type=str, help="Specifies a path from which the input should be taken. If not specified, input comes from STDIN and is terminated by EOF")
parser.add_argument("-m", "--method", nargs=1, type=method_int, help="Set the method for compressing. 0 = Build a string, 1 = Simple replacing, 2 = print the input in quotes. Normally the program uses the shortest of these")
parser.add_argument("-q", "--quiet", action="store_true", help="By default, CompressPy displays original and resulting byte count along with compression rate, this option disables it")
parser.add_argument("-e", "--exec", action="store_true", help="Instead of making a program that prints a message, the program instead executes it as Python code, using exec()")
parser.add_argument("-S", "--secure-exec", action="store_true", help="Sometimes the output contains a declaration of the variable s, which can occasionally result in program breaking when using --exec. This option makes the program delete that variable just before execution")
parser.add_argument("-s", "--status", action="store_true", help="Displays a dot on the screen every time an iteration is ran")
parser.add_argument("-3", "--use-python-3", action="store_true", help="Makes the program in Python3 instead of Python2, this will make the resulting program a bit longer, but can work together with --exec")

args = parser.parse_args()

if args.input != None:
    if os.path.exists(args.input[0]):
        try:
            text_orig = open(args.input[0], "r").read()
        except:
            print("Problem reading from the input file", file=sys.stderr)
            sys.exit()
    else:
        print("Can't find input file", file=sys.stderr)
        sys.exit()
else:
    # Read from stdin
    text_orig = sys.stdin.read()


text = text_orig

replaces = []


while 1:
    replace = findReplace(text)
    if replace == "":
        break
    ch = findReplaceChar(text)
    if ch == None:
        break
    if args.status:
        print(".", end="")
    text = text.replace(replace, ch)
    replaces.append(ch + replace)
if args.status:
    print("\nDone!")


possible_results = []


if args.use_python_3:
    action = lambda x: "print(" + x.strip() + ")"

    if args.exec:
        action = lambda x: "exec(" + x.strip() + ")"

else:
    action = lambda x: "print" + x

    if args.exec:
        action = lambda x: "exec" + x

joinCh = findReplaceChar("".join(replaces))

if args.exec and args.secure_exec:
    possible_results.append('s=' + quote(text) + '\nfor c in' + quote(joinCh.join(replaces[::-1])) + '.split("' + joinCh + '"):s=s.replace(c[0],c[1:])\n' + action(" 'del s\\n'+s"))
else:
    possible_results.append('s=' + quote(text) + '\nfor c in' + quote(joinCh.join(replaces[::-1])) + '.split("' + joinCh + '"):s=s.replace(c[0],c[1:])\n' + action(" s"))

possible_results.append(action(quote(text) + ".replace(" + ").replace(".join(quote(r[0]) + "," + quote(r[1:]) for r in replaces) + ")"))
possible_results.append(action(quote(text_orig)))

if args.use_python_3:
    possible_results.append(text_orig)


res = min(possible_results, key=len)
if args.method:
    res = possible_results[args.method[0]]

if args.output:
    try:
        output_file = open(args.output[0], "w")
        output_file.write(res)
        output_file.close()
    except:
        print("Problem writing to output file.", file=sys.stderr)
else:
    print(res)

if not args.quiet:
    print("Original length:", len(text_orig), file=sys.stderr)
    print("Compressed length:", len(res), file=sys.stderr)
    print("Compressed by %.2f%%" % (100 * (1 - len(res) / len(text_orig))), file=sys.stderr)

