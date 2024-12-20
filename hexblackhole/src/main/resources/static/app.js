const stompClient = new StompJs.Client({
  brokerURL: 'ws://localhost:8080/ws-connect'
});

stompClient.onConnect = (frame) => {
  setConnected(true);
  console.log('Connected: ' + frame);

  stompClient.subscribe('/subscribe/chat.' + $("#chatRoomId").val(), (message) => {
    let body = JSON.parse(message.body);
    let username = body.username;
    let content = body.content;
    showChat(username + ": " + content);
  });
};

function showChatHistory(chatRoomId) {
  let chatHistory = JSON.parse(localStorage.getItem('chatMessages_' + chatRoomId));
  if (chatHistory) {
    chatHistory.forEach((message) => {
      showChat(`${message.username}: ${message.content}`);
    });
  }
}

function sendChat() {
  stompClient.publish({
    destination: "/publish/chat." + $("#chatRoomId").val(),
    body: JSON.stringify({'username': $("#na").val(), 'content': $("#name").val()})
  });

  let currentChatHistory = JSON.parse(localStorage.getItem('chatMessages_' + $("#chatRoomId").val())) || [];

  if (stompClient.connected) { // 연결 상태일 때만 실행
    currentChatHistory.push({ username: $("#na").val(), content: $("#name").val() });
    localStorage.setItem('chatMessages_' + $("#chatRoomId").val(), JSON.stringify(currentChatHistory));
  }

  document.getElementById('name').value = '';
}

stompClient.onWebSocketError = (error) => {
  console.error('Error with websocket', error);
};

stompClient.onStompError = (frame) => {
  console.error('Broker reported error: ' + frame.headers['message']);
  console.error('Additional details: ' + frame.body);
};

function setConnected(connected) {
  $("#connect").prop("disabled", connected);
  $("#disconnect").prop("disabled", !connected);
  if (connected) {
    $("#conversation").show();
  }
  else {
    $("#conversation").hide();
  }
  $("#greetings").html("");
}

function connect() {
  stompClient.activate();
}

function disconnect() {
  stompClient.deactivate();
  setConnected(false);
  console.log("Disconnected");
}

function showChat(message) {
  $("#greetings").append("<tr><td>" + message + "</td></tr>");
}

$(function () {
  $("form").on('submit', (e) => e.preventDefault());
  $( "#connect" ).click(() => connect());
  $( "#disconnect" ).click(() => disconnect());
  $( "#send" ).click(() => sendChat());

  let chatRoomId = $("#chatRoomId").val();

  let currentChatHistory = JSON.parse(localStorage.getItem('chatMessages_' + chatRoomId)) || [];
  console.log(currentChatHistory)

    // 이전에 저장된 메시지 표시
    currentChatHistory.forEach(message => {
      showChat(message.username + ": " + message.content);
    });
  showChatHistory(chatRoomId);
});
