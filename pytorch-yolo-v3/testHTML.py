from yattag import Doc
import sys

imgNum = 0
divNum = 0
buttonNum = 0
h1Num = 0
pNum = 0


def checkShape(parameter, doc, tag, text):
    
    global imgNum, divNum, buttonNum, h1Num, pNum

    if parameter[0]=='img':
        with tag('div', id='photo-container'):
            doc.stag('img', src='C:/yolo/pytorch-yolo-v3/yattag-master/LGS.jpg', klass="img-thumbnail", id="img_"+ str(imgNum))
        imgNum = imgNum + 1    
    elif parameter[0]=='div':
        with tag('div', style = "background-color:lightblue", id="div_" + str(divNum)):
            text('Hello div!')
        divNum = divNum + 1
    elif parameter[0]=='button':
        with tag('button', onclick="alert('Hello Button!')", klass="btn btn-lg btn-primary", id="button_"+ str(buttonNum)):
            text("Click Me!")
        buttonNum = buttonNum + 1
    elif parameter[0]=='h1':
        with tag('h1', id = "h1_" + str(h1Num)):
            text('Capstone Project')
        h1Num = h1Num + 1
    elif parameter[0]=='p':
        with tag('p', id = "p_" + str(pNum)):
            text('P Tag')
        pNum = pNum + 1
    else: 
        print(0)
        



def writeHTML(*args):
    global imgNum, divNum, buttonNum, h1Num, pNum
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('head'):
            doc.stag('link', rel='stylesheet', href='bootstrap1.css')
            doc.stag('link', rel='stylesheet', href='test.css')
        with tag('body', id = 'hello'):
            for i in args:
                for j in i:
                    print(j, end='\n')
                    checkShape(j, doc, tag, text)
                imgNum = 0
                divNum = 0
                buttonNum = 0
                h1Num = 0
                pNum = 0
    """
    with tag('html'):
        with tag('body', id = 'hello'):

            checkShape()
            
            with tag('h1'):
                text('Hello world!')
            with tag('div', style = "background-color:lightblue"):
                text('Hello div!')
            with tag('button', onclick="alert('Hello Button!')"):
                text("Click Me!")
            with tag('div', id='photo-container'):
                doc.stag('img', src='C:/yolo/pytorch-yolo-v3/yattag-master/LGS.jpg', klass="photo")
            with tag('form', action = ""):
                doc.input(name = 'title', type = 'text')
                with doc.textarea(name = 'contact_message'):
                    pass
                doc.stag('input', type = 'submit', value = 'Send my message')
            """
#   print(doc.getvalue())

    file = open("C:/yolo/pytorch-yolo-v3/test.html",'w')
    file.write(doc.getvalue())
    file.close()
    

def writeCSS(*args):
    global imgNum, divNum, buttonNum, h1Num, pNum
    file = open("C:/yolo/pytorch-yolo-v3/test.css",'w')
    for i in args:
        for j in i:
            print(j, end='\n')
            pList = calcPosition(j[1], j[2], j[3], j[4], 1920, 1080)
            if j[0]=='img':
                tag='img#img_' + str(imgNum)
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
                tag='p#p_' + str(pNum)
                pNum = pNum + 1
            else: 
                continue        
            file.write(tag)
            file.write('{\n')
            file.write('position: absolute;\n')
            file.write('margin: 20px;\n')
            file.write('top: '+ str(pList[1]) + ';\n')
            file.write('left: '+ str(pList[0]) + ';\n')
            file.write('width: '+  str(pList[2]) + ';\n')
            file.write('height: '+ str(pList[3]) + ';\n')
            file.write('}\n')
        imgNum = 0
        divNum = 0
        buttonNum = 0
        h1Num = 0
        pNum = 0    
    file.close()
         
    
def calcPosition(c1x, c1y, c2x, c2y, screenWidth, screenHeight):
    htmlX = (int)((c1x/480) * screenWidth)
    htmlY = (int)((c1y/360) * screenHeight)
    shapeWidth = (int)((c2x - c1x) * screenWidth / 480)
    shapeHeight = (int)((c2y - c1y) * screenHeight / 360)
    positionList = [htmlX, htmlY, shapeWidth, shapeHeight]
    return positionList

