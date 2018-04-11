---
title: "Live Coding Shielding Problem"
teaching: 0
exercises: 90
questions:
- "How can I perform a shielding calculation using Python?"
keypoints:
- "Use Python to write a simple shielding calculation script."
- "Learn some best practices when writing Python."
objectives:
- "Produce a Python script from scratch"
- "Execute Python scripts in a command line"
- "Selection of appropriate data structures for an application"
- "Understand the value of using functions"
- "Learn best practices for function implementation"
- "Implement for loops to solve a problem"
---

## Shielding Problem 

In this lesson we'll be doing a live coding exercise in which we calculate the
uncollided flux on the other side of a heterogeneous shield composed of lead,
water, and tungsten. We'll be performing this calculation as a 1-D problem using
the following model:

$$ \huge \Phi = \Phi_{o} e^{-\mu x} $$

where 

 - $$ \Phi_{o} $$ - is the initial flux at the front of the shield (units: $$ cm^{-2}s^{-1} $$)
 - $$ \mu      $$ - is the attenuation coefficient of the shield (units: $$ cm^{-1} $$)
 - $$  x       $$ - is the shield thickness (units: $$ cm $$)
 - $$ \Phi     $$ - is the uncollided flux at the back of the shield (units: $$ cm^{-2}s^{-1} $$)

To begin, with a simple script which defines these variables and performs
the calculation for a shield with one material, lead, with a thickness of 15 cm.

<blockquote class="challenge">
<h2 id="script1"> Checkpoint 0 </h2>
  <div class="python highlighter-rogue"> 
    <div class="highlight">
      <pre class="highlight">
        <code>
{% include checkpoints/checkpoint0.py %} 
        </code>
      </pre>
    </div>
  </div>
  <p>
    To get the version of the script shown above, use
    <a href="https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint0.py"> this link </a>
  </p>
</blockquote>

The beginning of this script is a commented section of text describing what the
script does. Because this code is encased in triple-quoted (`"""`) both above
and below the text, Python will ignore this section and not treat it as
code. This is a nice way to put mult-line comments into your code instead of
starting each new line with a `#` symbol.

Next Python's built-in `math` module is imported into the script. Similar to the
built-in **functions** we discussed in [episode 2](/02-variables), Python comes
with a set of standard modules which add commonly needed capabilities to your
programs. In this case, we'll use the math module to access the exponential
function (`math.exp`). Notice, though, that when this function is called in
later lines it is called as `m.exp`. This is because we've imported the `math`
module **as** `m`. This is known as aliasing and is often used to shorten long
module names for convenience.

> ## Aliasing
> Aliasing is used to import a module under a different name, or alias.
> This is typically used to shorten the name of a module. The module will 
> behave the the same way under any name. For example:
> 
> ~~~
> import math
> math.cos(0.0)
> ~~~
> {: .python}
>
> will yield the same result as
>
> ~~~
> import math as m
> m.cos(0.0)
> ~~~
> {: .python}
>
{:.callout}

Next we initialize a few variables: `phi_0`, `mu`, and `x`. These represent the
initial flux, attenuation coefficient of lead, and the lead shield thicknes
respectiely. Finally, we perform the calculation for the uncollided flux
according to the model above and display the result on screen.

## Two Shields

Now let's update the script so that it reports the uncollided flux for another
shield composed of water. Perhaps the most straightforward way to do this is to
retype our code, but update the attenuation and thickness values to represent a 
water shield.

<blockquote class="challenge">
<h2 id="script1"> Checkpoint 1 </h2>
  <div class="python highlighter-rogue"> 
    <div class="highlight">
      <pre class="highlight">
        <code>
{% include checkpoints/checkpoint1.py %} 
        </code>
      </pre>
    </div>
  </div>
  <p>
    To get the version of the script shown above, use
    <a href="https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint1.py"> this link </a>
  </p>
</blockquote>

This is fairly straightforward, but what if we want to perform this computation 
10 times? 50 times? 10000 times? This small script would become large very quickly.
A good way to provide the ability to repeat this calculation is to create a function for 
calculating the flux given an attenuation coefficient and material thickness.

## Creating a function

In the code below, a function returning the flux for a shield (a $$\mu$$ and
$$x$$ value) has been implemented *and documented*. Underneath the line defining
the `calc_phi` function there is a set of text enclosed with triple-quotes
(`"""`) which contains information about the purpose of the function along with
its expected inputs and outputs. Triple quotes were used before to create
multi-line comments at the top of our script, but this comment block is special
because of its location in the code. Because this comment section appears right
below the function definition, it acts as documentation and is accessible from a
Python interpreter using the built-in `help` function. Specifically, executing
the command `help(calc_phi)` will display this information about the function on
screen.

Underneath this is the implementation of the function which computes the flux
value. 

<blockquote class="challenge">
<h2 id="script1"> Checkpoint 2 </h2>
  <div class="python highlighter-rogue"> 
    <div class="highlight">
      <pre class="highlight">
        <code>
{% include checkpoints/checkpoint2.py %} 
        </code>
      </pre>
    </div>
  </div>
  <p>
    To get the version of the script shown above, use
    <a href="https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint2.py"> this link </a>
  </p>
</blockquote>

## Correlating Shield Properties

For the purposes of today's exercise, the two pieces of information required to
define a shield are its attenuation coefficient, $$\mu$$, and its thickness,
$$x$$. Rather than separate these values in to different variable, a tuple can
be used to make sure these two properties will always be associated with each
other. Our function for this calculation now needs to be updated as well. 

<blockquote class="challenge">
<h2 id="script1"> Checkpoint 3 </h2>
  <div class="python highlighter-rogue"> 
    <div class="highlight">
      <pre class="highlight">
        <code>
{% include checkpoints/checkpoint3.py %} 
        </code>
      </pre>
    </div>
  </div>
  <p>
    To get the version of the script shown above, use
    <a href="https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint3.py"> this link </a>
  </p>
</blockquote>

As seen in the updated function documentation, the function `calc_phi` now takes
in only two arguments - the initial flux `phi_0` and an argument named
`mat_props`. Now when this argument is passed into the function we can unpack
the attenuation coefficient and shield thickness from `mat_props` variable and
perform our calculation. Note that if these lines were not being added in a
function, they would be added in the main body of the script for each shield
instead.

## A Two-Material Shield

Now that we have a function in place which returns the uncollided flux for a
single shield. We can explore that calculation for a multi-layer shield in the
code below. Because the material information is passed in as a list, it makes
the extension of this function for attenuation through multiple materials fairly
natural.  The calculation is performed for the first material and the resulting
flux value is passed into a calculation for the second material. Finally the
flux value is returned from the function and printed to screen in at the end of
the script. Note that this multi-material calculation now requires only one call
to the `calc_phi` function.


<blockquote class="challenge">
<h2 id="script1"> Checkpoint 4 </h2>
  <div class="python highlighter-rogue"> 
    <div class="highlight">
      <pre class="highlight">
        <code>
{% include checkpoints/checkpoint4.py %} 
        </code>
      </pre>
    </div>
  </div>
  <p>
    To get the version of the script shown above, use
    <a href="https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint4.py"> this link </a>
  </p>
</blockquote>

## A Multi-Material Shield

Our previous work made possible to calculate the flux after pasing through two
materials, but what about 5 materials? 10 materials? 

The design of the `calc_phi` function makes this possible with a relatively
small change to the code. Rather than asuuming a specific number of materials
are being passed into the function, we can use a for loop to calculate the flux
after each material and return the final flux value at the end of the function.


<blockquote class="challenge">
<h2 id="script1"> Checkpoint 5 </h2>
  <div class="python highlighter-rogue"> 
    <div class="highlight">
      <pre class="highlight">
        <code>
{% include checkpoints/checkpoint5.py %} 
        </code>
      </pre>
    </div>
  </div>
  <p>
    To get the version of the script shown above, use
    <a href="https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint5.py"> this link </a>
  </p>
</blockquote>

As demonstrated at the bottom of our code, this function can now be called to
calculate the uncollided flux at the end of an arbitrary set of shields with
varying thicknesses. It is also easy to set up different materials for the
calculation and use them interchangably.

[checkpoint0]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint0.py
[checkpoint1]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint1.py
[checkpoint2]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint2.py
[checkpoint3]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint3.py
[checkpoint4]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint4.py
[checkpoint5]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint5.py