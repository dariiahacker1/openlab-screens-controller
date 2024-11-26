import tuke_openlab

openlab = tuke_openlab.Controller(tuke_openlab.production_env())

openlab.screens.panel_2x2.set_url("https://pranx.com/hacker/")

for i in range(1,6):
    openlab.screens.vertical.get(i).set_url("https://pranx.com/hacker/")


