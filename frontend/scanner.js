const video = document.getElementById("video");
const status = document.getElementById("status");
const beep = document.getElementById("beep");

navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    video.srcObject = stream;
    video.play();
});

function sendToBackend(data) {
    fetch("https://YOUR_RENDER_URL/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ qr_data: data })
    })
    .then(res => res.json())
    .then(res => {
        if (res.status === "marked") {
            status.innerText = "Present Marked: " + res.student;
            beep.play(); // 🔊 SOUND
        }
    });
}