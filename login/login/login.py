import pynecone as pc

def index() -> pc.Component:
    pass

app = pc.App()
app.add_page(index)
app.compile()
