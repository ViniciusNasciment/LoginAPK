import pyrebase
import flet
from flet import *
import datetime
from functools import partial

config = {
    "apiKey": "AIzaSyBDCDmuPJQMDS_pOV3aV20i-3Ru2dOuZm0",
    "authDomain": "estudos-bf12f.firebaseapp.com",
    "projectId": "estudos-bf12f",
    "storageBucket": "estudos-bf12f.appspot.com",
    "messagingSenderId": "438346144007",
    "appId": "1:438346144007:web:34b7734c482381b8d14da2",
    "measurementId": "G-EJWN7E9V2Y",
    
    "databaseURL": "",
  }

# Initialize the Firebase app with your credentials
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

class UserWidget(UserControl):
    def __init__(self,
                 title:str,
                 sub_title:str,
                 btn_name:str,
                 func
            ):
                self.title = title
                self._sub_title = sub_title
                self.btn_name = btn_name
                self.func = func
                super().__init__()


    def InputTextField(self, text:str, hide: bool):
          return Container(
                alignment=alignment.center,
                content=TextField(
                      
                      height=48,
                      width=255,
                      bgcolor='#f0f3f6',
                      text_size=12,
                      color="black",
                      border_color="transparent",

                      hint_text=text,
                      filled=True,
                      cursor_color="black",
                      hint_style=TextStyle(
                            size=11,
                            color="black"
                        
                      ),
                      password=hide, #set to true or false to show/hide password
                      

                ),
          )

     # now we need the sign in/register button
    def signInOption(self, path:str,name:str):
          return Container(
            content=ElevatedButton(
                 content=Row(
                       alignment='center',
                       spacing=4,
                       controls=[
                             Image(
                                   src=path,
                                   width=30,
                                   height=30,

                             ),
                             Text(
                                   name,
                                   color='black',
                                   size=10,
                                   weight="bold",
                             ),
                       ],
                 ),
                    style = ButtonStyle(
                             shape={
                                   "":RoundedRectangleBorder
                                   (radius=8),
                             },
                             bgcolor={
                                   "": "white", ##COR DA BORDA DO FACEBOOK E GOOGLE
                             },
                       ),
                 ),
          )
    

    def build(self):
         

        self._title = Container(
            alignment=alignment.center,
            content=Text(
                self.title, # we will pass ins the args
                size=15,
                text_align="center",   ## TITULO PRINCIPAL
                weight="bold",
                color="black",

            ),
        )

        self._sub_title = Container(
             alignment=alignment.center,
             content=Text(
                   self._sub_title,
                   size=10,                  ## SUB TITULO
                   text_align="center",
                   color="black",
             )
        )

        # main sign-in UI here
        self._sign_in = Container(
              content=ElevatedButton(
                    on_click=partial(self.func),
                    content=Text(
                          self.btn_name,
                          size=11,
                          weight="bold"
                    ),
                    style=ButtonStyle(
                          shape={
                                "": RoundedRectangleBorder
                                (radius=8),
                          },
                          color={
                                "": "white",  ## LETRA DO BUTTON
                          },
                    ),
                    height=48,
                    width=255,
              )
        )

        # the UI that is returned from this class
        return Column(
              horizontal_alignment='center',
              controls=[
                    Container(padding=10),
                    self._title,
                    #
                    self._sub_title,
                    #
                    Column(
                          spacing=12,
                          controls=[
                                self.InputTextField("Email",
                                False),
                                self.InputTextField("Password",
                                True),
                          ],
                    ),
                    Container(padding=5),
                    self._sign_in,
                    Container(padding=5),
                        ## "Or continue with",
                    Column(
                          horizontal_alignment="center",
                          controls=[
                                Container(
                                      content=Text(
                                            "Or continue with",
                                            size=10,
                                            color="black",
                                      )
                                
                                ),
                                self.signInOption("facebook.png","Facebook"),
                                self.signInOption("GOOGLE.png","Google"),
                          ]
                    )
              ],
        )
    

def main(page:Page):
    # add some basic steup info
    page.title = "Flet with Firebase"
    page.bgcolor = "#f0f3f6"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    
    def _main_column_():
          return Container(
                width=280, 
                height=600,
                bgcolor="#ffffff",  ## COR DO FUNDO  DA CAIXA DE DIALOGO
                padding=12,
                border_radius=35,
                gradient=LinearGradient(['#808080','#fffafa']), #808080 #fffafa
                content=Column(
                      spacing=20,
                      horizontal_alignment="center"
                )
          )
    

    
    def _register_user(e):
          try:
                 auth.create_user_with_email_and_password(

                     _register_.controls[0].controls[3].controls[0].content.value,

                     _register_.controls[0].controls[3].controls[1].content.value
    

                )
                 print("Registration OK!")

          except Exception as e:
                print(e)


    def _sign_in(e):
          try:
                user = auth.sign_in_with_email_and_password(
                      
                    _sign_in_.controls[0].controls[3].controls[0].content.value,
                    _sign_in_.controls[0].controls[3].controls[1].content.value,     
                )

                info = auth.get_account_info(user["idToken"])

                data = ["createdAt","lastLoginAt",]

                for key in info:
                      if key == 'users':
                            for item in data:
                                  print(
                                        item
                                        + " "
                                        + datetime.datetime.fromtimestamp(
                                              int(info[key][0][item]) / 1000
                                        ).strftime("%D - %H:%M:%p")
                                  )
                _sign_in_.controls[0].controls[3].controls[0].content.value,
                _sign_in_.controls[0].controls[3].controls[1].content.value  
                _sign_in_.controls[0].controls[3].update

          except:
                print("Wrong email or password!")



    _sign_in_ = UserWidget(
          "Bem Vindo de volta!",

          "Insira os detalhes da sua conta abaixo.",
          "Entrar",

          _sign_in,
          
    )
    
    _register_ = UserWidget(
          "Crie Sua Account",
          "Cadastre seu e-mail e senha abaixo.",
          "Criar",
          _register_user,
    )
            

    _sign_in_main = _main_column_()
    _sign_in_main.content.controls.append((Container(padding=15)))
    _sign_in_main.content.controls.append(_sign_in_)

    _reg_main = _main_column_()
    _reg_main.content.controls.append((Container(padding=15)))
    _reg_main.content.controls.append(_register_)
    
    page.bgcolor = "#000000"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    

    page.add(
          Row(
                alignment='center',
                spacing=25,
                controls=[
                      _sign_in_main,
                      _reg_main,    
                ]
          )
    )


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")