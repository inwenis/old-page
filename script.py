
import os


WelcomeToMyPage = """
<td style="background-color: aqua;">
    <center>
        <h1>Welcome to <a href="./index.html">my page about Mandelbrot</a></h1>
    </center>
</td>"""

files = [x for x in os.listdir() if x.endswith('.html')]

for x in files:
    source = open(x)
    dest = open(f"out/{x}", "w")

    content = source.read()
    content = content.replace("{{WelcomeToMyPage}}", WelcomeToMyPage)
    dest.write(content)

    source.close()
    dest.close()

os.startfile(".\\out\\index.html")
