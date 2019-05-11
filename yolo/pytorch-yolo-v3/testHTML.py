from yattag import Doc
import sys


def writeHTML(*args):
    doc, tag, text = Doc().tagtext()
    i = 0
    for arg in args:
        print(arg[i], end='\n')
       # print("\n")
        i = i + 1 


    with tag('html'):
        with tag('body', id = 'hello'):
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

 #   print(doc.getvalue())

    file = open("C:/yolo/pytorch-yolo-v3/test.html",'w')
    file.write(doc.getvalue())
    file.close()
