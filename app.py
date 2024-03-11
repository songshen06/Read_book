from flask import Flask, render_template, request,send_file
from dialogues import pages  # 导入对话内容和页面信息
#import pyttsx4
import tempfile


app = Flask(__name__)

'''@app.route('/speak', methods=['POST'])
def speak():
    text = request.form.get('text')
    engine = pyttsx4.init()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
        engine.save_to_file(text, tmpfile.name)
        engine.runAndWait()  # 等待语音生成完成
    return send_file(tmpfile.name, as_attachment=True)
'''
@app.route('/', methods=['GET'])
def home():
    # 这是原来的首页路由处理函数
    selected_page = request.args.get('page', 'page2')  # 默认选中'page1'
    dialogues = pages.get(selected_page, {}).get('dialogues', [])
    image_file = pages.get(selected_page, {}).get('image', 'default.png')
    return render_template('index.html', dialogues=dialogues, image_file=image_file, pages=pages.keys())

@app.route('/read', methods=['GET'])
def read():
    # 新增的路由处理函数，用于渲染和访问read.html
    selected_page = request.args.get('page', 'page2')  # 同样默认选中'page1'
    dialogues = pages.get(selected_page, {}).get('dialogues', [])
    image_file = pages.get(selected_page, {}).get('image', 'default.png')
    return render_template('read.html', dialogues=dialogues, image_file=image_file, pages=pages.keys())

if __name__ == '__main__':
    app.run(debug=True, port=8080)
