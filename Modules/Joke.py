import pyjokes # via pip install pyjokes thru the terminal(can install any custom package)

jokes = pyjokes.get_jokes()
print(jokes)

# pipenv allows to install package based on each project so each project has its own
# virtual environments exist so that each project has access to specific packages that have been installed