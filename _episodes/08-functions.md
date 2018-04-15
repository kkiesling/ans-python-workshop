---
title: Creating Functions
teaching: 10
exercises: 0
questions:
- "How can I define new functions?"
- "What's the difference between defining and calling a function?"
- "What happens when I call a function?"
objectives:
- "Define a function that takes parameters."
- "Return a value from a function."
- "Explain why we should divide programs into small, single-purpose functions."
keypoints:
- "Define a function using `def function_name(parameter)`."
- "The body of a function must be indented."
- "Call a function using `function_name(value)`."
- "Numbers are stored as integers or floating-point numbers."
- "Integer division produces the whole part of the answer (not the fractional part)."
- "Variables defined within a function can only be seen and used within the body of the function."
- "If a variable is not defined within the function it is used, Python looks for a definition before the function call"
- "Use `help(thing)` to view help for something."
- "Put code whose parameters change frequently in a function, then call it with different parameter values to customize its behavior."
---

At this point,
we've written code to draw some interesting features in our inflammation data,
loop over all our data files to quickly draw these plots for each of them,
and have Python make decisions based on what it sees in our data.
But, our code is getting pretty long and complicated;
what if we had thousands of datasets,
and didn't want to generate a figure for every single one?
Commenting out the figure-drawing code is a nuisance.
Also, what if we want to use that code again,
on a different dataset or at a different point in our program?
Cutting and pasting it is going to make our code get very long and very repetitive,
very quickly.
We'd like a way to package our code so that it is easier to reuse,
and Python provides for this by letting us define things called 'functions' ---
a shorthand way of re-executing longer pieces of code.

Let's start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:

~~~
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
~~~
{: .language-python}

![The Blueprint for a Python Function](../fig/python-function.svg)

<!--- see https://gist.github.com/wd15/2b4ffbe5ce0d0ddb8a5b to
regenerate the above figure --->

The function definition opens with the keyword `def` followed by the
name of the function and a parenthesized list of parameter names. The
[body]({{ page.root }}/reference/#function-body) of the function --- the
statements that are executed when it runs --- is indented below the
definition line.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a [return statement]({{ page.root }}/reference/#return-statement) to send a result back to whoever asked for it.

Let's try running our function.

~~~
fahr_to_kelvin(32)
~~~

This command should call our function, using "32" as the input and return the function value.

In fact, calling our own function is no different from calling any other function:
~~~
print('freezing point of water:', fahr_to_kelvin(32))
print('boiling point of water:', fahr_to_kelvin(212))
~~~
{: .language-python}

~~~
freezing point of water: 273.15
boiling point of water: 373.15
~~~
{: .output}

We've successfully called the function that we defined,
and we have access to the value that we returned.

> ## Integer Division
>
> We are using Python 3, where division always returns a floating point number:
>
> ~~~
> $ python3 -c "print(5/9)"
> ~~~
> {: .language-python}
>
> ~~~
> 0.5555555555555556
> ~~~
> {: .output}
>
> Unfortunately, this wasn't the case in Python 2:
>
> ~~~
> 5/9
> ~~~
> {: .language-python}
>
> ~~~
> 0
> ~~~
> {: .output}
>
> If you are using Python 2 and want to keep the fractional part of division
> you need to convert one or the other number to floating point:
>
> ~~~
> float(5)/9
> ~~~
> {: .language-python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
>
> ~~~
> 5/float(9)
> ~~~
> {: .language-python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
>
> ~~~
> 5.0/9
> ~~~
> {: .language-python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
> ~~~
> 5/9.0
> ~~~
> {: .language-python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
>
> And if you want an integer result from division in Python 3,
> use a double-slash:
>
> ~~~
> 4//2
> ~~~
> {: .language-python}
>
> ~~~
> 2
> ~~~
> {: .output}
>
> ~~~
> 3//2
> ~~~
> {: .language-python}
>
> ~~~
> 1
> ~~~
> {: .output}
{: .callout}

## Composing Functions

Now that we've seen how to turn Fahrenheit into Kelvin,
it's easy to turn Kelvin into Celsius:

~~~
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

print('absolute zero in Celsius:', kelvin_to_celsius(0.0))
~~~
{: .language-python}

~~~
absolute zero in Celsius: -273.15
~~~
{: .output}

What about converting Fahrenheit to Celsius?
We could write out the formula,
but we don't need to.
Instead,
we can [compose]({{ page.root }}/reference/#compose) the two functions we have already created:

~~~
def fahr_to_celsius(temp_f):
    temp_k = fahr_to_kelvin(temp_f)
    result = kelvin_to_celsius(temp_k)
    return result

print('freezing point of water in Celsius:', fahr_to_celsius(32.0))
~~~
{: .language-python}

~~~
freezing point of water in Celsius: 0.0
~~~
{: .output}

This is our first taste of how larger programs are built:
we define basic operations,
then combine them in ever-large chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here --- typically half a dozen to a few dozen lines --- but
they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.

> ## Readable Code
>
> Revise a function you wrote for one of the previous exercises to try to make
> the code more readable. Then, collaborate with one of your neighbors
> to critique each other's functions and discuss how your function implementations
> could be further improved to make them more readable.
{: .challenge}
