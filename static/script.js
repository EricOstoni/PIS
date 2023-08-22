function addMeter() {
  const data = {
    owner: document.getElementById("owner").value,
    street: document.getElementById("street").value,
    city: document.getElementById("city").value,
    state: document.getElementById("state").value,
  };

  fetch("/add_meter", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => alert(data.message));
}

function deleteMeter() {
  const id = document.getElementById("delete_id").value;

  fetch("/delete_meter/" + id, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((data) => alert(data.message));
}

function filterMeters() {
  let date = document.getElementById("filter_date").value;
  let city = document.getElementById("filter_city").value;

  let url = "/filter?";
  if (date) url += "date=" + date;
  if (city) {
    if (date) url += "&";
    url += "city=" + city;
  }

  fetch(url)
    .then((response) => response.json())
    .then((data) => populateTable(data));
}

function getAllMeters() {
  fetch("/filter")
    .then((response) => response.json())
    .then((data) => populateTable(data));
}

function populateTable(data) {
  let tableBody = document.getElementById("meterTable");
  tableBody.innerHTML = "";

  for (let meter of data) {
    let row = `
            <tr>
                <td>${meter.id}</td>
                <td>${meter.owner}</td>
                <td>${meter.street}</td>
                <td>${meter.city}</td>
                <td>${meter.state}</td>
                <td>${meter.date_measured}</td>
            </tr>
        `;

    tableBody.innerHTML += row;
  }
}

function editMeter() {
  const data = {
    owner: document.getElementById("edit_owner").value,
    street: document.getElementById("edit_street").value,
    city: document.getElementById("edit_city").value,
    state: document.getElementById("edit_state").value,
  };

  const meterId = document.getElementById("edit_id").value;

  fetch("/edit_meter/" + meterId, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.message);

      getAllMeters();
    });
}
