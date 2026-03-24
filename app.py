import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from rag import process_pdf, create_vectorstore, get_answer

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

vectorstore = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    global vectorstore
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    chunks = process_pdf(filepath)
    vectorstore = create_vectorstore(chunks)
    return jsonify({'message': 'PDF processed successfully!'})

@app.route('/ask', methods=['POST'])
def ask_question():
    global vectorstore
    if vectorstore is None:
        return jsonify({'error': 'Please upload a PDF first!'}), 400
    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided!'}), 400
    answer = get_answer(vectorstore, question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)