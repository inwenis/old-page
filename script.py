import os
import shutil
import sys


WelcomeToMyPage = """
<td style="background-color: aqua;">
    <center>
        <h1>Welcome to <a href="./index.html">my page about Mandelbrot</a></h1>
    </center>
</td>"""

NavigationBar = """
<td>
    <ul>
        <li><a href="./index.html">Home</a></li>
        <li><a href="./image.html">Cool Image</a></li>
        <li><a href="./script.html">Script</a></li>
        <li><a href="./about.html">About</a></li>
    </ul>
</td>
"""

MainContent = """
 <p>
    The <strong>Mandelbrot set</strong> is one of the most iconic and fascinating objects in mathematics,
    known for its intricate, self-similar structure and its deep connection to chaos and complexity.
    At its core, the Mandelbrot set is a collection of complex numbers that produce stable behavior
    when repeatedly fed into a simple iterative function:
  </p>

  <pre><code>z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c</code></pre>

  <p>
    Here, <code>z</code> and <code>c</code> are complex numbers, and the process starts with <code>z₀ = 0</code>.
    A point <code>c</code> is in the Mandelbrot set if this sequence does <em>not</em> diverge to infinity
    no matter how many times the function is applied.
  </p>

  <p>
    Visually, the Mandelbrot set is often plotted in the complex plane, with the x-axis representing the
    real part and the y-axis the imaginary part of <code>c</code>. What emerges is a black, cardioid-shaped
    figure with countless bulbous attachments and infinitely complex boundary regions. Points inside the
    set are colored black, while points outside it are typically colored based on how quickly they "escape"
    to infinity, producing spectacular, colorful fractal patterns.
  </p>

  <p>
    One of the most remarkable aspects of the Mandelbrot set is its <strong>self-similarity</strong>.
    As you zoom into its boundary, you discover repeating motifs, miniature versions of the entire set,
    and seemingly endless complexity—no matter how far you zoom, there’s always more detail. However, it’s
    not exactly repeating; the self-similarity is <em>quasi-self-similar</em>, meaning similar patterns
    recur with variations, adding to its allure and richness.
  </p>

  <p>
    Beyond its beauty, the Mandelbrot set has become a symbol of how simple rules can lead to incredibly
    complex behavior—a cornerstone idea in chaos theory. It's also an example of how abstract mathematics
    (in this case, complex dynamics) can produce visual forms that are not only striking but endlessly
    thought-provoking.
  </p>
"""

files = [x for x in os.listdir() if x.endswith('.html')]

shutil.rmtree('out', ignore_errors=True)
os.makedirs('out')

for x in files:
    source = open(x)
    dest = open(f"out/{x}", "w")

    content = source.read()
    content = content\
        .replace("{{WelcomeToMyPage}}", WelcomeToMyPage)\
        .replace("{{NavigationBar}}", NavigationBar)\
        .replace("{{MainContent}}", MainContent)
    dest.write(content)

    source.close()
    dest.close()

if len(sys.argv) > 1:
    if sys.argv[1] == "build":
        pass
    else:
        os.startfile(f".\\out\\{sys.argv[1]}")
else:
    os.startfile(".\\out\\index.html")
