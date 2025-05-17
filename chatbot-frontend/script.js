const baseURL = "http://localhost:5000"; 

function appendMessage(sender, text) {
  const chatbox = document.getElementById("chatbox");
  const message = document.createElement("div");
  message.className = `message ${sender}`;
  message.innerText = `${sender === 'user' ? 'You' : 'Bot'}: ${text}`;
  chatbox.appendChild(message);
  chatbox.scrollTop = chatbox.scrollHeight;
}

async function handleUserMessage() {
  const input = document.getElementById("userInput");
  const userMessage = input.value.trim();
  if (!userMessage) return;

  appendMessage("user", userMessage);
  input.value = "";

  try {
    const response = await fetch(`${baseURL}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage, location: "delhi" }) // or "bangalore"
    });

    const data = await response.json();
    appendMessage("bot", data.response);
  } catch (err) {
    appendMessage("bot", "⚠️ Error connecting to backend.");
    console.error("Fetch error:", err);
  }
}
