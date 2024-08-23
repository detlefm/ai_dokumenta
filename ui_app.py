from ctkgui import Window
from xlib.x_openai import ask_openai
from chat_result import Chat_Result
from dotenv import load_dotenv

load_dotenv(".env")


class App:

    def __init__(self):
        self.window = Window(title="Chat App",geometry="800x800",on_submit=self.chat)

    def chat(self,txt:str,filenames:list[str]):
        completion = ask_openai(prompt=txt,source=filenames)
        result = Chat_Result.from_completion(completion=completion)
        content = result.content_all
        #outstr = (txt+'\n') + "\n".join(filenames)
        self.window.write_result(content)
        self.window.change_status_label(f'Token {result.token}, Done ...')

    def run(self):
        self.window.mainloop()




if __name__ == "__main__":
    App().run()