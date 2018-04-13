---
title: "Running and Quitting"
teaching:  5
exercises: 0
questions:
- "How can I run Python programs?"
objectives:
- "Launch iPython."
- "Run some simple python commands."
- "Exit the iPython interpreter."
keypoints:
- "Use iPython for editing and running Python."
- "Use the keyboard and mouse to select and edit cells."

---
## Python programs are plain text files.

*   They have the `.py` extension to let everyone (including the operating system)
    know it is a Python program.
    *   This is convention, not a requirement.


## Start iPython


~~~
$ ipython
~~~
{: .python}

*   This will start a iPython interpreter.
*   The iPython interpreter provides several advantages over the standard Python interpreter:
    * Tab completion allows you to easily access the names of things you are
      using and learn more about them
    * Smart up-down history allows you to quickly access and re-run old commands
    * Use of some simple terminal commands like ls, cd, pwd, etc.
    * Inline help documentation using "?"

## The iPython interpreter


## A few simple commands

Upon executing the iPython command, the following prompt will appear at the
bottom of your screen.

~~~
In [1]:
~~~
{: .python}

The `In` portion indicates that iPython is waiting for input and the `[1]`
indicates that this is the first command we'll run in the iPython session.

Let's start by running a few simple commands to get a feel for interacting with
this interpreter.

Type the following command and press return.

~~~
In [1]: 2 + 7
~~~
{: .python}

After pressing return you should see something like the following.

~~~
Out [1]: 9
~~~
{: .output}

Here the `Out` is indicating that this is the output from the code we executed
in command `[1]`.

For the remainder of the workshop, these lessons won't include the input/output
portions shown here but rather just the commands and resulting output.


> ## Installing iPython on your own machine
> *   The [Anaconda package manager][anaconda] is an automated way to install the iPython on your own machine.
>     *   See [the setup instructions]({{ page.root }}/setup/) for Anaconda installation instructions.
> *   It also installs all the extra libraries it needs to run.
> *   Once you have installed Python and the iPython requirements, open a shell and type:
{: .callout}


[anaconda]: https://docs.continuum.io/anaconda/install
[jupyter]: http://jupyter.org/
[markdown]: https://en.wikipedia.org/wiki/Markdown
