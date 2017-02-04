
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
