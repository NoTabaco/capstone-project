html = """
<table border=1>
    <tr>
        <th>Number</th>
        <th>Square</th>
    </tr>
    <indent>
    <% for i in range(10): %>
        <tr>
            <td><%= i %></td>
            <td><%= i**2 %></td>
        </tr>
    </indent>
</table>
"""

with open("C:/yolo/pytorch-yolo-v3/webTest.html", "w") as file:
    file.write(html)