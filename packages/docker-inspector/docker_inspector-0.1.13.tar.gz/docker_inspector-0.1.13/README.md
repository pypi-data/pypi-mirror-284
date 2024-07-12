```
  _____             _                           
 |  __ \           | |                          
 | |  | | ___   ___| | _____ _ __               
 | |  | |/ _ \ / __| |/ / _ \ '__|              
 | |__| | (_) | (__|   <  __/ |                 
 |_____/ \___/ \___|_|\_\___|_|                 
  _____                           _             
 |_   _|                         | |            
   | |  _ __  ___ _ __   ___  ___| |_ ___  _ __ 
   | | | '_ \/ __| '_ \ / _ \/ __| __/ _ \| '__|
  _| |_| | | \__ \ |_) |  __/ (__| || (_) | |   
 |_____|_| |_|___/ .__/ \___|\___|\__\___/|_|   
                 | |                            
                 |_|                        
```

# Installation

Install pipx:
```shell
apt install pipx
pipx ensurepath
```

Install docker-inspector via pipx:
```shell
pipx install docker-inspector
dinspect
```

# Development

Run locally:

 - `textual console -x EVENT -x DEBUG`
 - `textual run --dev docker_inspector.app:run`

Publish:

`poetry publish --build`
