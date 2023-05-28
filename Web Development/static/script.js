const tag = document.getElementById("body")
let arr = ["Greeting 1", "Greeting 2", "Greeting 3"]
window.onload(() => {
    tag.innerHTML = arr[Math.floor(Math.random() * arr.length)]
})