
import os


WelcomeToMyPage = """
<td style="background-color: aqua;">
    <center>
        <h1>Welcome to <a href="./index.html">my page about Mandelbrot</a></h1>
    </center>
</td>"""

f = open("index.html")
content = f.read()
f.close()
content = content.replace("{{WelcomeToMyPage}}", WelcomeToMyPage)

f = open("out/index.html", "w")
f.write(content)
f.close()

os.startfile(".\\out\\index.html")
