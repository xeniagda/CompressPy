
# CompressPy

This is a simple program that can compress files by making them into small Python programs.


## How to use:

    python3 CompressPy.py [-h] [-o PATH] [-i PATH] [-q] [-e] [-s] [-3]

Options are:

* `-h, --help`: Display the help message. The help is basically the same as this section.
* `-o PATH, --output PATH`: The output destination for the resulting program. If not specified, output goes to STDOUT.
* `-i PATH, --input PATH`: Specifies a path from which the input should be taken.  If not specified, input comes from STDIN and is terminated by EOF.
* `-q, --quiet`: By default, `CompressPy` displays original and resulting byte count along with compression rate, this option disables it.
* `-e, --exec`: Instead of making a program that prints a message, the program instead executes it as Python code, using `exec`.
* `-S, --secure-exec`: Sometimes the output contains a declaration of the variable s, which can occasionally result in program breaking when using --exec. This option makes the program delete that variable just before execution.
* `-s, --status`: Displays a dot on the screen every time an iteration is ran.
* `-3, --use-python-3`: Makes the program in Python3 instead of Python2, this will make the resulting program a bit longer, but can work together with --exec..
* `-h (--help)`: Display help.
* `-o (--output) PATH`: Sets the output destination. Default is STDOUT.
* `-i (--input) PATH`: Specifies the input path. Default is STDIN.
* `-q (--quiet)`: By default, `CompressPy` displays original and resulting byte count along with compression rate, this option disables it..
* `-s (--status)`: Makes `CompressPy` print a dot for every iteration. Can be useful for displaying progress..
* `-e (--exec)`: Instead of the resulting program printing the input, the program instead executes the input. Can be used with the `--use-python-3` flag to generate runnable Python 3 code..
* `-3 (--use-python-3)`: Makes the resulting code runnable in Python 3 instead of Python 2.

# Please note that this program can be very slow for large inputs.

## How the algorithm works:

The inner workings of this program is rather simple. Basically, all it does is finds a segment in the text that repeats itself a lot, and replaces that text with something shorter, and then in the resulting program, replacing that shorter bit back into the original segment.

For example, if the input is: `Java 1.0, Java 1.1, Java 1.2, Java 1.3`, we could replace `Java 1.` with something else, like `!`, making the text `!0, !1, !2, !3`.

We repeat this process for as long as it's effective, and the shortest of three programs that replace back all the shortened signs back into the original corresponding segment. These programs are:

```python
print"shortened_text".replace("sign1","segment1").replace("sign2","segment2")...etc
```

```python
s="shortened_text"
for c in "sign1segment1:sign2segment2:sign3segment3...".split(":"):s=s.replace(c[0],c[1:])
print s
```

```python
print"original_text"
```

In each of these programs, `shortened_text` is the text with all the shortened signs in place, `signN` and `segmentN` are the n-th sign and segment (`!` and `Java 1.` in our example above), and also, in the second case, the `:` doesn't have to be a `:`, it can be any character really. The last case is just there in case the compression wasn't effective, it doesn't have any overhead and only expands the input by a little bit.

If the `--use-python-3` flag is used, `print ` is replaced by `print()`, and if the `--exec` flag is used, `print` is replaced with `exec`.

