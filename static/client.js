function generateUserId() {
    return 'user_' + Math.floor(Math.random() * 10000);  // e.g. user_1234
}
const currentUserId = generateUserId()
const ws = new WebSocket(`ws://${location.host}/ws?user_id=${currentUserId}`)

ws.onopen = () => {
    console.log('Connected to the WebSocket server.');
    console.log(currentUserId)
};

ws.onmessage = (event) => {
    console.log('onmessage', event.data);
    const messages = document.getElementById('messages');
    const msg = document.createElement('li');

    const messageData = JSON.parse(event.data);
    msg.className = messageData.userId === currentUserId ? 'my-message' : 'peer-message'

    msg.textContent = `${messageData.userId}: ${messageData.text}`;  
    messages.appendChild(msg)
}

document.getElementById('send').onclick = () => {
 const input = document.getElementById('msg');
  console.log('Sending message:', input.value);  
  ws.send( input.value )
  input.value = '';
}