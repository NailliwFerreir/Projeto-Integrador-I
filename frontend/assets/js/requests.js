//Requests
const url = "http://127.0.0.1:5000";
const textSelect =
  'Selecione <span class="select-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>';
function selectBoxValue(e) {
  document.querySelector(".option-alter .select-selected").innerHTML = e;
  let alterButton = document.querySelector(".option-alter button");
  alterButton.setAttribute("onclick", `makePutRequest(${e})`);
}
function selectBoxValue2(e) {
  document.querySelector(".option-delete .select-selected").innerHTML = e;
  let deleteButton = document.querySelector(".choose-delete button");
  deleteButton.setAttribute("onclick", `makeDeleteRequest(${e})`);
}
async function makePostRequest() {
  let co = document.getElementById("insert-co").value;
  let so2 = document.getElementById("insert-so2").value;
  let no2 = document.getElementById("insert-no2").value;
  let o3 = document.getElementById("insert-o3").value;
  let mp25 = document.getElementById("insert-mp25").value;
  let mp10 = document.getElementById("insert-mp10").value;
  if ((co && so2 && no2 && mp10 && mp25 && o3) === "") {
    window.alert("Preencha todos os campos!");
    return 0;
  }
  const item = {
    co: parseFloat(co.replace(",", ".")),
    so2: parseFloat(so2.replace(",", ".")),
    no2: parseFloat(no2.replace(",", ".")),
    o3: parseFloat(o3.replace(",", ".")),
    mp25: parseFloat(mp25.replace(",", ".")),
    mp10: parseFloat(mp10.replace(",", ".")),
  };
  await fetch(`${url}/sample`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  })
    .then((response) => response.json())
    .then(() => {
      document.getElementById("insert-co").value = "";
      document.getElementById("insert-so2").value = "";
      document.getElementById("insert-no2").value = "";
      document.getElementById("insert-o3").value = "";
      document.getElementById("insert-mp25").value = "";
      document.getElementById("insert-mp10").value = "";
      window.alert("Amostra Inserida!");
    })
    .finally(async () => {
      await makeGetRequest();
      await getClassificationInfo();
    })
    .catch((error) => console.log(`Error is : ${error}`));
}
async function makeGetRequest() {
  const tbody = document.querySelector(".table-rows");
  const optionAlter = document.querySelector(".option-alter .select-items");
  const optionDelete = document.querySelector(".option-delete .select-items");
  tbody.innerHTML = "";
  optionAlter.innerHTML = "";
  optionDelete.innerHTML = "";
  await fetch(`${url}/samples`)
    .then((response) => response.json())
    .then((json) => {
      samples = json["samples"];
      for (let i in samples) {
        let newRowTable = document.createElement("div");
        newRowTable.setAttribute("class", "table-row");
        newRowTable.innerHTML = `<div class="table-cell">${samples[i][0]}</div><div class="table-cell">${samples[i][1]}</div><div class="table-cell">${samples[i][2]}</div><div class="table-cell">${samples[i][3]}</div><div class="table-cell">${samples[i][4]}</div><div class="table-cell">${samples[i][5]}</div><div class="table-cell">${samples[i][6]}</div>`;
        tbody.append(newRowTable);
      }
      for (let id in samples) {
        let newOption = document.createElement("div");
        newOption.innerHTML = samples[id][0];
        newOption.setAttribute("class", "select-item");
        newOption.setAttribute("data-value", samples[id][0]);
        newOption.setAttribute("onclick", `selectBoxValue(${samples[id][0]})`);
        optionAlter.appendChild(newOption);
        let newOtherOption = document.createElement("div");
        newOtherOption.innerHTML = samples[id][0];
        newOtherOption.setAttribute("class", "select-item");
        newOtherOption.setAttribute("data-value", samples[id][0]);
        newOtherOption.setAttribute(
          "onclick",
          `selectBoxValue2(${samples[id][0]})`
        );
        optionDelete.appendChild(newOtherOption);
      }
    })
    .catch((error) => console.log(`Error is : ${error}`));
}
async function makePutRequest(code) {
  if (
    document.querySelector(".option-alter .select-selected").innerHTML ===
    textSelect
  ) {
    window.alert("Por favor selecione o ID");
    return;
  }
  let co = document.getElementById("alter-co").value;
  let so2 = document.getElementById("alter-so2").value;
  let no2 = document.getElementById("alter-no2").value;
  let o3 = document.getElementById("alter-o3").value;
  let mp25 = document.getElementById("alter-mp25").value;
  let mp10 = document.getElementById("alter-mp10").value;
  if ((co && so2 && no2 && mp10 && mp25 && o3) === "") {
    window.alert("Preencha todos os campos!");
    return 0;
  }
  const item = {
    co: parseFloat(co.replace(",", ".")),
    so2: parseFloat(so2.replace(",", ".")),
    no2: parseFloat(no2.replace(",", ".")),
    o3: parseFloat(o3.replace(",", ".")),
    mp25: parseFloat(mp25.replace(",", ".")),
    mp10: parseFloat(mp10.replace(",", ".")),
  };
  await fetch(`${url}/sample/${code}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  })
    .then((response) => response.json())
    .then(() => {
      document.querySelector(".option-alter .select-selected").innerHTML =
        textSelect;
      document.getElementById("alter-co").value = "";
      document.getElementById("alter-so2").value = "";
      document.getElementById("alter-no2").value = "";
      document.getElementById("alter-o3").value = "";
      document.getElementById("alter-mp25").value = "";
      document.getElementById("alter-mp10").value = "";
      window.alert("Amostra alterada!");
    })
    .finally(async () => {
      await makeGetRequest();
      await getClassificationInfo();
    })    .catch((error) => console.log(error));
}
async function makeDeleteRequest(code) {
  if (
    document.querySelector(".option-delete .select-selected").innerHTML ===
    textSelect
  ) {
    window.alert("Por favor selecione o ID");
    return;
  }
  fetch(`${url}/samples/${code}`, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      document.querySelector(".option-alter .select-selected").innerHTML =
        textSelect;
      document.querySelector(".option-delete .select-selected").innerHTML =
        textSelect;
      window.alert("Amostra excluída!");
    })
    .finally(async () => {
      await makeGetRequest();
      await getClassificationInfo();
    })
    .catch((error) => console.log(error));
}
async function getClassificationInfo() {
  document.querySelector(".classification button").innerHTML = "Recalcular";
  fetch(`${url}/classificacao`)
    .then((response) => response.json())
    .then((json) => {
      console.log(json["result"][0]);
      document.querySelector(".classification .option-title").innerHTML =
        "Qualidade do ar: " + json["result"][0];
      console.log(json["result"][1]);
      document.querySelector(
        ".classification .text"
      ).innerHTML = `${json["result"][1]}`;
      document.getElementById('classif-mp10').innerHTML = json["average"][0];/* <br/> MP10 (${json["average"][0]}), MP25 (${json["average"][1]}), O3 (${json["average"][2]}), CO (${json["average"][3]}), NO2 (${json["average"][4]}), SO2 (${json["average"][5]}) */
      document.getElementById('classif-mp25').innerHTML = json["average"][1];
      document.getElementById('classif-o3').innerHTML = json["average"][2];
      document.getElementById('classif-co').innerHTML = json["average"][3];
      document.getElementById('classif-no2').innerHTML = json["average"][4];
      document.getElementById('classif-so2').innerHTML = json["average"][5];
      document.getElementById('blocks').style.display = 'flex';
    })
    .catch((err) => console.log(err));
}

makeGetRequest();
