document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('modal');
    const closeModal = document.getElementsByClassName('close')[0];

    modal.style.display = 'none';

    document.getElementById('get-id-btn').addEventListener('click', function() {
        const fbLink = document.getElementById('fb-link').value;
        const modalTitle = document.getElementById('modal-title');
        const modalMessage = document.getElementById('modal-message');

        modalTitle.innerHTML = 'Fetching ID...';
        modalMessage.innerHTML = '';
        modal.style.display = 'flex';

        fetch('/facebook-id-retriever/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ link: fbLink })
        })
        .then(response => response.json().then(data => ({status: response.status, body: data})))
        .then(({status, body}) => {
            if (status === 200 && body.Sukses) {
                modalTitle.innerHTML = 'Sukses';
                modalMessage.innerHTML = `Facebook ID is ${body.Message}!`;
            } else {
                modalTitle.innerHTML = 'Gagal';
                modalMessage.innerHTML = `${body.Message}!`;
            }
        })
        .catch(error => {
            modalTitle.innerHTML = 'Error';
            modalMessage.innerHTML = `${error}`;
        });

        closeModal.onclick = function() {
            modal.style.display = 'none';
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var placeholders = [
        "Example : https://www.facebook.com/share/p/...?",
        "Example : https://www.facebook.com/...?",
        "Example : https://www.facebook.com/groups/...?"
    ];
    var randomIndex = Math.floor(Math.random() * placeholders.length);
    document.getElementById('fb-link').placeholder = placeholders[randomIndex];
});