from app import app, db
from app.models import User,Post

@app.shell_context_processor
def make_shell_context():
    """
    通過添加數據庫實例和模型來創建一個shell上下文環境
    (透過shell_context_processor裝飾器函數註冊為一個shell上下文函數)
    flask shell 命令運行時 會調用此函數並在shell繪畫中註冊他返回的項目
    返回一個字典 對每個項目需要透過字典的鍵提供一個名稱以便在shell中調用
    """
    return {'db': db, 'User': User, 'Post': Post}