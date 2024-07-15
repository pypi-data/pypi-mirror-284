from vncdotool import api

class VNC:
    def __init__(self, host:str, port:int, password:str=None):
        self.client = api.connect(f"{host}::{port}", password=password)
    
    def mouseMove(self, x, y, step:int=None):
        """移动鼠标到指定位置, step是拖动的步长, 不设置则一步到位"""
        if step == None:
            self.client.mouseMove(x, y)
        else:
            self.client.mouseDrag(x, y, step)
    
    def mouseClickLeft(self):
        """点击鼠标左键"""
        self.client.mousePress(1)
    
    def mouseClickRight(self):
        """点击鼠标右键"""
        self.client.mousePress(3)
    
    def mouseDownLeft(self):
        """按下鼠标左键"""
        self.client.mouseDown(1)
    
    def mouseUpLeft(self):
        """放开鼠标左键"""
        self.client.mouseUp(3)

    def mouseDownRight(self):
        """按下鼠标右键"""
        self.client.mouseDown(3)
    
    def mouseUpLeft(self):
        """放开鼠标右键"""
        self.client.mouseUp(1)

    def shift(self, key:str):
        """按下并放开shift-{key}"""
        self.client.keyPress(f"shift-{key}")
    
    def ctrl(self, key:str):
        """按下并放开ctrl-{key}"""
        self.client.keyPress(f"ctrl-{key}")

    def ctrlAltDel(self):
        """按下并放开 ctrl-alt-del"""
        self.client.keyPress(f"ctrl-alt-del")

    def keyPress(self, key:str):
        """
        按下并放开按键
        举例来说, key可以是
        1. a
        2. 5
        3. .
        4. enter
        5. shift-a
        6. ctrl-C
        7. ctrl-alt-del
        """
        self.client.keyPress(key)

    def keyDown(self, key:str):
        """
        按下按键
        举例来说, key可以是
        1. a
        2. 5
        3. .
        4. enter
        5. shift-a
        6. ctrl-C
        7. ctrl-alt-del
        """
        self.client.keyDown(key)
    
    def keyUp(self, key:str):
        """
        放开按键
        举例来说, key可以是
        1. a
        2. 5
        3. .
        4. enter
        5. shift-a
        6. ctrl-C
        7. ctrl-alt-del
        """
        self.client.keyUp(key)
    
    def captureScreen(self, fname:str):
        """保存屏幕截图到文件, 图片文件支持jpg,jpeg,gif,png结尾"""
        self.client.refreshScreen()
        self.client.captureScreen(fname)

    def captureRegion(self, fname:str, x:int, y:int, w:int, h:int):
        """保存屏幕的区域的截图到文件"""
        self.client.refreshScreen()
        self.client.captureRegion(fname, x, y, w, h)

    def input(self, string:str):
        """通过模拟按键输入字符串"""
        for c in string:
            self.keyPress(c)

    def close(self):
        """关闭VNC连接"""
        self.client.disconnect()
        api.shutdown()

# 示例用法
if __name__ == "__main__":
    vnc_host = '192.168.1.5::5900'
    vnc_password = 'redhat'
    x = 234
    y = 234

    
    client = VNCClient(vnc_host, vnc_password)
    # client.move(x, y)
    # client.click()
    # client.move(x + 50, y + 50)
    # client.click_right()
    # client.ctrl('c')
    # client.input('Hello, World!')
    # client.key('c')
    # client.captureScreen("240715.vnc.jpg")
    client.paste("oooooooooooooooooo")
    client.close()