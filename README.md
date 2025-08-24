# Project Overview

**An asynchronous chat room where multiple users can send messages in real time. It uses:**
**aiohttp** for HTTP server and WebSocket support
**asyncio** for concurrent non-blocking I/O
**Jinja2** templates for the initial HTML page
<!-- -->
# Features
<ul>
  <li>
    Real-time messaging (both ways)
  </li>
   <li>
     Each client is given unique userID when using the session
  </li>
   <li>
      Modern styling with css
  </li>
</ul>

# Prerequisites 
<ul>
  <li>
     Python 3.7+
  </li>
   <li>
      aiohttp and aihttp_jinja2
  </li>
</ul>

# File structure 
```
.
├── app.py             # aiohttp server & routes
├── handlers.py        # Server logic    
├── templates
│   └── index.html     # Jinja2 template
├── static
    ├── client.js      # WebSocket client logic
    └── main.css       # Styling
```
# Installation
```
git clone https://github.com/yourusername/async-chat-app.git
cd async-chat-app
```
<!-- -->
**install dependencies and create virtual envoronment** 
```
python3 -m venv venv
source venv/bin/activate
pip install aiohttp aiohttp_jinja2
```
<!-- -->
# Run the app
```
python3 app.py
```
<!-- -->

# Example of the usage
<img width="1103" height="985" alt="image" src="https://github.com/user-attachments/assets/65e9da52-d5a3-4f0f-85f7-5a2b38ab8010" />
<img width="1038" height="970" alt="image" src="https://github.com/user-attachments/assets/4b7cef89-c610-4368-b0ec-ce0ef4a8e724" />

