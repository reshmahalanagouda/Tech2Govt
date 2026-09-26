class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }
        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        // FIX - Force small size, don't block page
        if(chatBox){
            chatBox.style.width = "350px";
            chatBox.style.height = "450px";
            chatBox.style.position = "fixed";
            chatBox.style.bottom = "80px";
            chatBox.style.right = "30px";
            chatBox.style.left = "auto";
            chatBox.style.top = "auto";
            chatBox.style.zIndex = "1000";
            chatBox.style.display = "none"; // Hidden at start
            chatBox.style.opacity = "1";
            chatBox.style.pointerEvents = "auto";
        }

        openButton.addEventListener('click', () => this.toggleState(chatBox))
        sendButton.addEventListener('click', () => this.onSendButton(chatBox))
        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;
        // FIX - Show/hide properly without blocking
        if(this.state) {
            chatbox.style.display = "flex";
            chatbox.classList.add('chatbox--active')
            // Make sure it stays small on phone
            if(window.innerWidth < 600){
                chatbox.style.width = "90%";
                chatbox.style.right = "5%";
                chatbox.style.height = "60vh";
            }
        } else {
            chatbox.style.display = "none";
            chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }
        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);
        fetch($SCRIPT_ROOT + '/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "Sam", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''
        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam")
            {
                html += '<div class="messages_item messages_item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages_item messages_item--operator">' + item.message + '</div>'
            }
          });
        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();
