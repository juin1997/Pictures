#coding:utf-8
from flask import Flask, request, jsonify,render_template,send_from_directory,send_file,make_response
from PIL import Image, ImageDraw, ImageFont  
import json

def create_app():
  app = Flask(__name__)
  return app

application = create_app()
PICTURE_FOLDER = '/root/picture/pictures'

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/getPicture', methods = ['POST'])
def picture():
    try:
        data = request.get_data()  
        dict = json.loads(data)
        name = dict['name']
        filename = name + ".jpg"
        imge = Image.open(PICTURE_FOLDER+"/model.jpg")
        draw = ImageDraw.Draw(imge)  
        fillcolor = 'black'  
        myfont = ImageFont.truetype(u"STKAITI.TTF",size=50)
        width, height = imge.size  
        draw.text((width-200, height-200), name, font=myfont, fill=fillcolor)
        im.save(PICTURE_FOLDER + "/" + filename, 'JPEG') 
        return jsonify({'finished': 'true'})
    except: 
        return jsonify({'finished': 'false'})

@application.route('/picture/<filename>', methods = ['GET'])
def returnPicture(filename):
    filename = filename + ".jpg"  
    response = make_response(send_file(PICTURE_FOLDER+"/"+filename))
    response.headers["Content-Disposition"] = "attachment; filename=picture.jpg;"
    return response

if __name__ == '__main__':
    application.run()