function playAudio(text) {
    fetch("/synthesize", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({ text: text })
    })
    .then(response => response.blob())
    .then(blob => {
        const audio = new Audio(URL.createObjectURL(blob));
        const visualizer = document.querySelector(`#viz-${[...document.querySelectorAll("li")].findIndex(li => li.innerText.includes(text)) + 1}`);
        visualizer.classList.add("playing");

        audio.onended = () => {
            visualizer.classList.remove("playing");
        };

        audio.play();
    });
}
