---
title: "Live Coding Shielding Problem"
teaching: 0
exercises: 90
questions:
- "How can I perform a shielding calculation using Python?"
keypoints:
- "Use Python to write a simple shielding calculation script."
- "Learn some best practices when writing Python."
---
## Shielding Problem 

In this lesson we'll be doing a live coding exercise in which we calculate the
uncollided flux on the other side of a heterogeneous shield composed of lead,
plastic, and tungsten. We'll be performing this calculation as a 1-D problem using
the following model:

$$ \huge \Phi = \Phi_{o} e^{-\mu x} $$

where 

 - $$ \Phi_{o} $$ - is the initial flux at the front of the shield (units: $$ cm^{-2}s^{-1} $$)
 - $$ \mu      $$ - is the attenuation coefficient of the shield (units: $$ cm^{-1} $$)
 - $$  x       $$ - is the shield thickness (units: $$ cm $$)
 - $$ \Phi     $$ - is the uncollided flux at the back of the shield (units: $$ cm^{-2}s^{-1} $$)

To begin, with a simple script which defines these variables and performs
the calculation for a shield with one material, lead, with a thickness of 15 cm.


~~~
{% include checkpoints/checkpoint0.py %}
~~~

> ## Getting this script
> To get the version of the script shown above, use [this link][checkpoint0]
>
{: .callout}

[checkpoint0]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint0.py
[checkpoint1]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint1.py
[checkpoint2]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint2.py
[checkpoint3]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint3.py
[checkpoint4]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint4.py
[checkpoint5]: https://raw.githubusercontent.com/kkiesling/ans-python-workshop/gh-pages/_includes/checkpoints/checkpoint5.py

