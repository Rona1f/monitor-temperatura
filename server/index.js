const express = require('express');
const app = express();
app.use('/static', express.static('static'))
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

var devices = {
  
}

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/json', (req, res) =>{
  res.json(devices)
})



io.on('connection', (socket) => {
  for(var element in devices) {
    io.emit('message', devices[element])
  }
  console.log('conectado')
  socket.on('message', (msg)=>{
      devices[msg['dispositivo']] = msg
      devices[msg['dispositivo']]['hora'] = Date.now()
      console.log(msg)
      io.emit('message', msg)

  })
});

server.listen(80, () => {
  console.log('listening on *:80');
});
