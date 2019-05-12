from yattag import Doc
import sys

def checkShape(parameter, doc, tag, text): 
    if parameter[0]=='Star':
        with tag('div', id='photo-container'):
            doc.stag('img', src='C:/yolo/pytorch-yolo-v3/yattag-master/LGS.jpg', klass="img-thumbnail")
    elif parameter[0]=='Rectangle':
        with tag('div', style = "background-color:lightblue"):
            text('Hello div!')
    elif parameter[0]=='Ellipse':
        with tag('button', onclick="alert('Hello Button!')", klass="btn btn-lg btn-primary"):
            text("Click Me!")
    elif parameter[0]=='Circle':
        with tag('h1'):
            text('Capstone Project')
    else: 
        print(0)
        



def writeHTML(*args):
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('head'):
            doc.stag('link', rel='stylesheet', href='bootstrap1.css')
        with tag('body', id = 'hello'):
            for i in args:
                for j in i:
                    print(j, end='\n')
                    checkShape(j, doc, tag, text)
            
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
    file = open("C:/yolo/pytorch-yolo-v3/test.css",'w')
    for i in args:
        for j in i:
            print(j, end='\n')
            pList = calcPosition(j[1], j[2], j[3], j[4], 1920, 1080)
            if j[0]=='Star':
                tag='img'    
            elif j[0]=='Rectangle':
                tag='div'
            elif j[0]=='Ellipse':
                tag='button'
            elif j[0]=='Circle':
                tag='h1'
            else: 
                continue
            file.write(tag)
            file.write('{\n')
            file.write('position: absolute;\n')
            file.write('top: '+ str(pList[1]) + ';\n')
            file.write('left: '+ str(pList[0]) + ';\n')
            file.write('width: '+  str(pList[2]) + ';\n')
            file.write('height: '+ str(pList[3]) + ';\n')
            file.write('}\n')
    file.close()
         
    
def calcPosition(c1x, c1y, c2x, c2y, screenWidth, screenHeight):
    htmlX = (int)((c1x/480) * screenWidth)
    htmlY = (int)((c1y/360) * screenHeight)
    shapeWidth = (int)((c2x - c1x) * screenWidth / 480)
    shapeHeight = (int)((c2y - c1y) * screenHeight / 360)
    positionList = [htmlX, htmlY, shapeWidth, shapeHeight]
    return positionList
