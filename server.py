import os
from flask import Flask, render_template, request, jsonify, send_file
app = Flask(__name__, template_folder='template')

@app.route('/uploadfile', methods = ['GET'])
def upload_file():
   return render_template('upload.html')

@app.route('/downloads', methods = ['GET'])
def download_file():
   return render_template('fileviewer.html')

@app.route('/download/<filename>', methods = ['GET'])
def download(filename):
   return send_file("uploads/"+str(filename))

@app.route('/files',methods = ['GET'])
def get_files_in_folder():
   return jsonify(get_files())
	
@app.route('/uploader', methods = ['POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      os.mkdir("downloads")
      f.save("downloads/"+f.filename)
      return 'file uploaded successfully'

def get_files():
   files = os.listdir("uploads")
   files = [f for f in files if os.path.isfile("uploads/"+f)]
   return files
		
def run():
    app.run(host="0.0.0.0", port=5000)

run()