let MessageTextArea = document.getElementById("Message")
let SendMessageButton = document.getElementById("SendMessage")

function Sleep(Time) {
	return new Promise(resolve => setTimeout(resolve, Time));
}

function Back() {
	window.location.href = "index.html"
}

function SendMessage() {
	if (MessageTextArea.value.length > 0) {
		fetch("https://discord.com/api/webhooks/1161641929004564550/-9y70-L94x0zD9Yt1eMTNRH4KAZ15TBZ7FjG6-LD8dxkFHJS8vmm9akMysw4NTThtGxD", {
			method: "post",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ content: MessageTextArea.value })
		})
		MessageTextArea.value = ""
		SendMessageButton.value = "Sent!"
		Sleep(1000).then(() =>
			SendMessageButton.value = "Send"
		)
	}
}
