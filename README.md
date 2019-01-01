# Web-APP Personal Notes and Demo
This repo is a personal practice follow [Liao's tutorial about deploy web apps based on jinja2 and ngix](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339210950e063b4795d574036bc5dcf0c2449bc52000). 
I make some modification changes for deeper understanding of deploy a web app. 

During learning form this repo, some points need to be noticed.
+ If the generator and calling process are not both coroutine, the python will raise error such as call functiuons from non-async generators. So please always use the function with {async def, await [function name]/yield from [function name]
+ Before use this repository please establish mysql database with user name, database name and table under database. Then modify the [config file](/WEB/config_default.py)
