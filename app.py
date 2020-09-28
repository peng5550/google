import base64
import hashlib
import hmac
import struct
import time
import tkinter
from tkinter import Button, Entry, Label, END
import tkinter.font as tf
import pyperclip


class Application(object):

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Google")

        # 设置窗口大小和位置
        self.window.geometry('500x250+90+66')
        self.window.wm_attributes('-topmost', 1)
        # 设置字体
        self.font = tf.Font(size=15)

        # 谷歌秘钥
        self.label_secret = Label(self.window, text="谷歌秘钥")
        self.label_secret.place(x=40, y=50, width=60, height=30)

        # 秘钥输入框
        self.input_secret = Entry(self.window, font=self.font, textvariable=tkinter.StringVar())
        self.input_secret.place(x=120, y=50, width=230, height=30)
        self.input_secret.bind("<Return>", self.btn_event)

        # 查询button
        self.btn = Button(self.window, text="查询", command=self.btn_event)
        self.btn.place(x=385, y=50, width=100, height=30)

        # 谷歌验证码
        self.label_captcha = Label(self.window, text="谷歌验证码")
        self.label_captcha.place(x=40, y=120, width=60, height=30)

        # 验证码结果
        self.result_captcha = Entry(self.window, font=self.font, textvariable=tkinter.StringVar())
        self.result_captcha.place(x=120, y=120, width=230, height=30)

    def getGoogleCode(self, secretKey):
        if not secretKey:
            return "Input Error."
        try:
            decoded_secretKey = base64.b32decode(secretKey, True)
            interval_number = int(time.time() // 30)
            message = struct.pack(">Q", interval_number)
            digest = hmac.new(decoded_secretKey, message, hashlib.sha1).digest()
            index = ord(chr(digest[19])) % 16
            googleCode = (struct.unpack(">I", digest[index:index + 4])[0] & 0x7fffffff) % 1000000
            return "%06d" % googleCode

        except Exception as e:

            return "Input Error."

    def btn_event(self, *args):
        secret = self.input_secret.get().strip()
        googleCode = self.getGoogleCode(secret)
        self.result_captcha.delete(0, END)
        self.result_captcha.insert(END, googleCode)
        pyperclip.copy(googleCode)
        self.input_secret.delete(0, END)

    def run(self):

        self.window.mainloop()


if __name__ == '__main__':
    app_ = Application()
    app_.run()
