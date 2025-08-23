
const ws = new WebSocket(`ws://${location.host}/ws`)
ws.onopen = () => {
    console.log('Connected to the WebSocket server.');
};
ws.onmessage = (event) => {
  console.log('onmessage', event.data)
  const messages = document.getElementById('messages');
  const msg = document.createElement('li');

  msg.textContent = event.data;
  messages.appendChild(msg);
}

document.getElementById('send').onclick = () => {
 const input = document.getElementById('msg');
  console.log('Sending message:', input.value);  
  ws.send(input.value);
  input.value = '';
}