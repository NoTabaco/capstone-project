from yattag import Doc
import sys

imgNum = 0
divNum = 0
buttonNum = 0
h1Num = 0
pNum = 0

def checkShape(parameter, doc, tag, text):
    
    global imgNum, divNum, buttonNum, h1Num, pNum
    convertKeyword1 = 'aria-pressed'
    convertKeyword2 = 'aria-label'
    convertKeyword3 = 'data-mdc-ripple-is-unbounded'

    imgString = """\
 <div class="mdc-card demo-card demo-card--hero">
    <div class="mdc-card__primary-action mdc-ripple-upgraded" tabindex="0" style="--mdc-ripple-fg-size:210px; --mdc-ripple-fg-scale:2.34115; --mdc-ripple-fg-translate-start:-31.5px, 129.188px; --mdc-ripple-fg-translate-end:70px, 60.4375px;">
        <div class="mdc-card__media mdc-card__media--16-9 demo-card__media" style="background-image: url(&quot;https://material-components.github.io/material-components-web-catalog/static/media/photos/3x2/2.jpg&quot;);">
        </div>
        <div class="demo-card__primary">
            <h2 class="demo-card__title mdc-typography--headline6">Our Image</h2>
        </div>
        <div class="demo-card__primary">
            <h3 class="demo-card__subtitle mdc-typography--subtitle2">by AGH KJM</h3>
        </div>
        <div class="demo-card__secondary mdc-typography--body2">Image Contents Web design Visit My Project.</div>
    </div>
</div>
"""       
    pString = """\
  <div class="input-wrapper">
        <input type="text" placeholder = "Enter your name">
        <label>Enter your name</label>
    </div>
"""
    
    divString = """\
    <div class="bg-dark mr-md-3 pt-3 px-3 pt-md-5 px-md-5 text-center text-white overflow-hidden">
        <div class="my-3 p-3">
            <h2 class="display-5">Another headline</h2>
            <p class="lead">And an even wittier subheading.</p>
        </div>
        <div class="bg-light shadow-sm mx-auto" style = "width: 80%; height: 30%; border-radius: 21px 21px 0 0;"></div>
    </div>
"""

    if parameter[0]=='img':
        with tag('div', id ="img_"+ str(imgNum)):
            doc.asis(imgString)
        imgNum = imgNum + 1    
    elif parameter[0]=='div':
        with tag('div', id="div_" + str(divNum)):
            doc.asis(divString)
        divNum = divNum + 1
    elif parameter[0]=='button':
        with tag('button', onclick="alert('Hello Button!')", klass="mdc-button mdc-button--outlined", id="button_"+ str(buttonNum)):
            text("Click Me! ")
        buttonNum = buttonNum + 1
    elif parameter[0]=='h1':
        with tag('h1', id = "h1_" + str(h1Num), style = "font-family: \"Montserrat\", sans-serif"):
            text('Capstone Project')
        h1Num = h1Num + 1
    elif parameter[0]=='p':
        with tag('div', id = "p_" + str(pNum)):
            doc.asis(pString)
        pNum = pNum + 1
    else: 
        print(0)
        

def writeHTML(*args):
    global imgNum, divNum, buttonNum, h1Num, pNum
    scriptString = "<script src = \"https://unpkg.com/material-components-web@latest/dist/material-components-web.min.js\"></script>"
    refreshString = "<meta http-equiv= refresh content = 1>"
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('head'):
            #doc.asis(refreshString)
            doc.stag('link', rel='stylesheet', href='https://www.w3schools.com/w3css/4/w3.css')
            doc.stag('link', rel='stylesheet', href='https://fonts.googleapis.com/css?family=Montserrat')
            doc.stag('link', rel='stylesheet', href='https://fonts.googleapis.com/icon?family=Material+Icons')
            doc.stag('link', rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
            doc.stag('link', rel='stylesheet', href='https://unpkg.com/material-components-web@latest/dist/material-components-web.min.css')
            doc.stag('link', rel='stylesheet', href='https://getbootstrap.com/docs/4.3/dist/css/bootstrap.min.css', integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T', crossorigin = 'anonymous')
            doc.stag('link', rel='stylesheet', href='https://getbootstrap.com/docs/4.3/examples/product/product.css')
            doc.stag('link', rel ='stylesheet', href= 'Img_css.css')
            doc.stag('link', rel ='stylesheet', href= 'P_css.css')
            doc.stag('link', rel='stylesheet', href='test.css')
        with tag('body', id = 'hello'):
            with tag('div', id='container'):
                for i in args:
                    for j in i:
                        print(j, end='\n')
                        checkShape(j, doc, tag, text)
                    imgNum = 0
                    divNum = 0
                    buttonNum = 0
                    h1Num = 0
                    pNum = 0  
            doc.asis(scriptString)

#   print(doc.getvalue())

    file = open("C:/yolo/pytorch-yolo-v3/test.html",'w')
    file.write(doc.getvalue())
    file.close()

cssString = """\
@media screen and (max-width:980px){
    #container{
        display: flex;
        width:100%;
    }
}

@media screen and (max-width:700px){
    #container{
        display: block;
    }
    #container button {
        display: block;
        position: relative;
        float: none;
        width: 300px;
        top: auto;
        left: auto;
        
    }
    #container h1 {
        display: block;
        position: relative;
        float: none;
        width: 300px;
        top: auto;
        left: auto;
    }
    #container img {
        display: block;
        position: relative;
        float: none;
        width: 300px;
        top: auto;
        left: auto;
    }
    #container div {
        position: relative;
        float: none;
        width: 300px;
        top: auto;
        left: auto;
    }
    #container p {
        display: block;
        position: relative;
        float: none;
        width: 300px;
        top: auto;
        left: auto;
    }
}
"""

def writeCSS(*args, cssWidth, cssHeight):
    global imgNum, divNum, buttonNum, h1Num, pNum, cssString
    file = open("C:/yolo/pytorch-yolo-v3/test.css",'w')
    for i in args:
        for j in i:
            pList = calcPosition(j[1], j[2], j[3], j[4], cssWidth, cssHeight)
            if j[0]=='img':
                tag='div#img_' + str(imgNum)
                imgNum = imgNum + 1    
            elif j[0]=='div':
                tag='div#div_' + str(divNum)
                divNum = divNum + 1
            elif j[0]=='button':
                tag='button#button_' + str(buttonNum)
                buttonNum = buttonNum + 1
            elif j[0]=='h1':
                tag='h1#h1_' + str(h1Num)
                h1Num = h1Num + 1
            elif j[0]=='p':
                tag='div#p_' + str(pNum)
                pNum = pNum + 1
            else: 
                continue        
            file.write(tag)
            file.write('{\n')
            file.write('display: flex;\n')
            file.write('position: absolute;\n')
            file.write('text-align: center;\n')
            file.write('margin: 20px;\n')
            file.write('top: '+ str(pList[1]) + '%;\n')
            file.write('left: '+ str(pList[0]) + '%;\n')
            file.write('width: '+  str(pList[2]) + '%;\n')
            file.write('height: '+ str(pList[3]) + '%;\n')
            file.write('}\n')
        imgNum = 0
        divNum = 0
        buttonNum = 0
        h1Num = 0
        pNum = 0
    file.write(cssString)    
    file.close()

def calcPosition(c1x, c1y, c2x, c2y, width, height):
    htmlX = (int)((c1x/width) * 100)
    htmlY = (int)((c1y/height) * 100)
    shapeWidth = (int)((c2x - c1x) / width * 100)
    shapeHeight = (int)((c2y - c1y) / height * 100)
    positionList = [htmlX, htmlY, shapeWidth, shapeHeight]
    return positionList
