from microdot import Microdot

app = Microdot()

@app.route('/')
async def index(request):
    return 'Hello, world!'

app.run()

#	https://raw.githubusercontent.com/miguelgrinberg/microdot/main/src/microdot/microdot.py