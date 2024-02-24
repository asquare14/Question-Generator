const form = document.querySelector('form');
const deleteButton = document.getElementsByClassName("material-icons-round")[0];

const createChatElement = (content, className) => {
    const chatDiv = document.createElement("div");
    chatDiv.classList.add("chat", className);
    chatDiv.innerHTML = content;
    return chatDiv;
}

const createChatContent = (imgSrc, altText, strongText, pText) => `
    <div class="chat-content">
        <div class="chat-details" style="display: flex; align-items: center;">
            <img src="${imgSrc}" alt="${altText}" style="margin-right: 10px;">
            <div>
               <strong> ${strongText} </strong>
                <p>${pText}</p>
            </div>
        </div>
    </div>`;

const handleFormSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const chatContainer = document.querySelector(".chat-container");

    // display loader
    document.getElementById('loader').style.display = 'block';

    // outgoing chat
    const outgoingChatDiv = createChatElement(createChatContent("https://cdn-icons-png.flaticon.com/512/10753/10753869.png", "user-img", "You", formData.get('context')), "outgoing");
    chatContainer.appendChild(outgoingChatDiv);

    // incoming chat
    const incomingChatDiv = createChatElement(createChatContent("https://cdn-icons-png.flaticon.com/512/6134/6134346.png", "chatbot-img", "Q-GPT", ""), "incoming");
    chatContainer.appendChild(incomingChatDiv);

    const incomingChatText = document.createElement("p");

    fetch('/generate-question', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // hide loader
        document.getElementById('loader').style.display = 'none';

        if (data.hasOwnProperty('error')) {
            incomingChatText.classList.add("error");
            incomingChatText.textContent = data.error;
        } else {
            incomingChatText.textContent = data.question;
        }
        incomingChatDiv.querySelector(".chat-details").appendChild(incomingChatText);
        chatContainer.scrollTo(0, chatContainer.scrollHeight);
        event.target.reset();
    })
    .catch(console.error);
};

form.addEventListener('submit', handleFormSubmit);

deleteButton.addEventListener("click", () => {
    document.getElementById('generated-questions').innerHTML = "";
});