
import os


WelcomeToMyPage = """
<td style="background-color: aqua;">
    <center>
        <h1>Welcome to <a href="./index.html">my page about Mandelbrot</a></h1>
    </center>
</td>"""

NavigationBar = """
<td>
    <ul>
        <li><a href="./page1.html">Item 1</a></li>
        <li><a href="./page2.html">Item 2</a></li>
        <li><a href="./page3.html">Item 3</a></li>
    </ul>
</td>
"""

files = [x for x in os.listdir() if x.endswith('.html')]

for x in files:
    source = open(x)
    dest = open(f"out/{x}", "w")

    content = source.read()
    content = content.replace("{{WelcomeToMyPage}}", WelcomeToMyPage).replace("{{NavigationBar}}", NavigationBar)
    dest.write(content)

    source.close()
    dest.close()

os.startfile(".\\out\\index.html")
