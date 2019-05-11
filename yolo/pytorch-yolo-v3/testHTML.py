from yattag import Doc
import sys

def checkShape(parameter, doc, tag, text): 
    if parameter[0]=='Star':
        with tag('div', id='photo-container'):
            doc.stag('img', src='C:/yolo/pytorch-yolo-v3/yattag-master/LGS.jpg', klass="photo")
    elif parameter[0]=='Rectangle':
        with tag('div', style = "background-color:lightblue"):
            text('Hello div!')
    elif parameter[0]=='Ellipse':
        with tag('button', onclick="alert('Hello Button!')"):
            text("Click Me!")
    elif parameter[0]=='Circle':
        with tag('h1'):
            text('Hello world!')
    else: 
        print(0)
        



def writeHTML(*args):
    doc, tag, text = Doc().tagtext()
    with tag('html'):
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
