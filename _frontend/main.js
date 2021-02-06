var container = document.getElementById("content")
var form1 = document.getElementById("main-input")


url = "http://127.0.0.1:5000/api/v1/todos"
sendRequest = () => {
    fetch(url).then(resp => resp.json()).then(data => {
        for (let i = 0; i < data.length; i++) {
            if (data[i].completed == true) {
                container.innerHTML += `<li class="list-group-item">
                <input type="checkbox" checked onClick=toggle(${data[i].id});>
                ${data[i].title}
                <a href="#" class="glyphicon glyphicon-remove" onClick=deletToDo(${data[i].id});></a>
            </li>`
            } else {
                container.innerHTML += `<li class="list-group-item">
                <input type="checkbox" onClick=toggle(${data[i].id});>
                ${data[i].title}
                <a href="#" class="glyphicon glyphicon-remove" onClick=deletToDo(${data[i].id});></a>
            </li>`
            }

        }
    })
}
sendRequest()


deletToDo = (id) => {
    let iDD = {
        "id": id
    }
    fetch(url, {
        method: "DELETE",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(iDD)
    }).then(resp => resp.json()).then(data => {
        console.log(data);
    })
}

toggle = (id) => {
    let idD = {
        "id": id
    }
    fetch(url, {
        method: "PUT",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(idD)
    }).then(resp => resp.json()).then(data => {
        console.log(data);
    })
}

posted = (title) => {
    let iii = {
        "title": title
    }
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(iii)
    }).then(resp => resp.json()).then(data => {
        console.log(data);
    })
}


form1.addEventListener("change",function(){
    var test = form1.value
    posted(test)
})
