import pynecone as pc
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

# firebase config
config = {
    apiKey: os.getenv('apiKey'),
    authDomain: os.getenv('authDomain'),
    projectId: os.getenv('projectId'),
    storageBucket: os.getenv('storageBucket'),
    messagingSenderId: os.getenv('messagingSenderId'),
    appId: os.getenv('appId'),
    measurementId: os.getenv('measurementId')
}

# pyrebase init
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()  # gives access to firebase auth

# main state class


class State(pc.state):
    pass

def user_sign_in(self):
    try:
        # authenticate user
        user = auth.sign_in_with_email_and_password(
            self.email_value,
            self.password_value,
        )
        # if user is registered
        if user["registered"]:
            # change UI color scheme
            print(registered)
    except Exception as e:
        # change UI color scheme
        pass

# input field
def get_input_field(icon: str, placeholder: str, _type: str):
    return pc.container(
        # horizontally stack icon and input field
        pc.hstack(
            pc.icon(
                tag=icon,
                color="white",
                fontSize="11px",
            ),
            pc.input(
                placeholder=placeholder,
                border="0px",
                focus_border_color="None",
                color="white",
                fontWeight="semibold",
                fontSize="11px",
                type=_type,
            ),
        ),
        # container settings
        borderBottom="0.1px solid gray",
        width="300px",
        height="45px",
    )


def index():
    main_container = pc.container(

        # vertical stack for input fields and buttons
        pc.vstack(
            pc.container(height="65"),
            pc.container(
                pc.text(
                    "Sign In",
                    fontSize="20px",
                    color="white",
                    fontWeight="bold",
                    letterSpacing="2px",
                ),
                # text settings
                width="250px",
                center_content=True
            ),

            pc.container(
                pc.text(
                    "Made with 🤍 using Pynecone",
                    fontSize="12px",
                    color="white",
                    fontWeight="#eeeeee",
                    letterSpacing="0.25px",
                ),
                # text settings
                width="250px",
                center_content=True
            ),
            # padding
            pc.container(height="50px"),

            # custom text fields
            get_input_field("email", "Email", ""),
            pc.container(height="5px"),

            # password input field
            get_input_field("lock", "Password", "password"),
            pc.container(height="5px"),

            # forgot password
            pc.container(
                pc.text(
                    "Forgot Password",
                    color="white",
                    fontSize="12px",
                    textAlign="end",
                )
            ),
            pc.container(height="55px"),

            # form button
            pc.container(
                pc.button(
                    pc.text(
                        "Sign In",
                        color="white",
                        weight="bold",
                        on_double_click=lambda: State.user_sign_in()
                    ),
                    # button settings
                    width="300px",
                    height="45px",
                    color_scheme="blue"
                ),
            ),
        ),

        # container settings
        width="400px",
        height="75vh",
        center_content=True,
        bg="1D2330",
        borderRadius="15px",
        boxShadow="41px -41px 82px #0d0f15, -41px 41px 82px #2d374b",

    )

    # main stack to return
    _main = pc.container(
        main_container,
        # stack settings
        center_content=True,
        justifyContent="center",
        maxWidth="auto",
        height='100vh',
        bg="#1D2330"
    )

    # return main stack
    return _main


app = pc.App()
app.add_page(index)
app.compile()
