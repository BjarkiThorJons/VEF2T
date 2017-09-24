<!DOCTYPE html>
    <html>
        <head>
            <title></title>
        </head>
        <body>
        <form action="/senda" method="post">
            <h1>Upplýsingar</h1>
            <label>Nafn:</label><br>
            <input type="text" name="nafn" required=""><br>
            <label>Heimilisfang:</label><br>
            <input type="text" name="heimilisfang" required=""><br>
            <label>Email:</label><br>
            <input type="email" name="email" required=""><br>
            <label>Sími:</label><br>
            <input type="number" name="simi" required=""><br>
            <h1>Pizzu særð</h1>
            <input type="radio" name="staerd" value="1000" checked> 9 tommur 1000kr<br>
            <input type="radio" name="staerd" value="1200"> 12 tommur 1200kr<br>
            <input type="radio" name="staerd" value="1900"> 18 tommur 1900<br>
            <h1>Álegg</h1>
            <input type="checkbox" name="alegg" value="200">Ananas<br>
            <input type="checkbox" name="alegg" value="200">Bacon<br>
            <input type="checkbox" name="alegg" value="200">Skinka<br>
            <input type="checkbox" name="alegg" value="200">Peperoni<br>
            <input type="submit" value="Panta">
        </form>
        </body>
    </html>
