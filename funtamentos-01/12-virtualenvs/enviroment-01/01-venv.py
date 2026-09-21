#  python3 -m venv venv 
# to create the venv

# to list 
# pip list 

# pip freeze > requirements.txt 
# to send the version to send 

#  source venv/bin/activate
# to activate the venv

from cowpy import cow

vaca = cow.Cowacter()

print(vaca.milk("Pythonnnn.."))