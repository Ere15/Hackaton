document.addEventListener("DOMContentLoaded", function() {
    var filterBtn = document.getElementById("filter-btn");
    var dropdownContent = document.querySelector(".dropdown-content");
    var searchBtn = document.getElementById("search-btn");
    var searchInput = document.getElementById("search");
    var notFoundMessage = document.getElementById("not-found");

    // Показываем/скрываем выпадающее меню при клике на кнопку "Фильтр"
    filterBtn.addEventListener("click", function() {
        dropdownContent.classList.toggle("show");
    });

    // Обработчик для фильтрации по выбранным меткам
    var labels = document.querySelectorAll(".dropdown-content input[type='checkbox']");
    labels.forEach(function(label) {
        label.addEventListener("change", filterRows);
    });

    // Обработчик для поиска при нажатии на кнопку лупы
    searchBtn.addEventListener("click", filterRows);

    // Обработчик для поиска при вводе в поле поиска
    searchInput.addEventListener("input", filterRows);

    // Обработчик для открытия новой страницы при клике на строку запроса
    var requestRows = document.querySelectorAll(".requests-table tbody tr");
    requestRows.forEach(function(row) {
        row.addEventListener("click", function(event) {
            var cell = event.target.closest("td"); // Находим ячейку, на которой был клик
            if (cell.cellIndex === 1) { // Проверяем, что клик был на ячейке "Название"
                var requestData = row.cells[0].textContent; // Получаем данные запроса из первой ячейки (номер запроса)
                // Формируем URL новой страницы
                var newPageURL = "request_details.html?request=" + encodeURIComponent(requestData);
                // Открываем новую страницу в этой же вкладке
                window.location.href = newPageURL;
            }
        });
    });

    function filterRows() {
        var searchText = searchInput.value.toLowerCase();
        var rows = document.querySelectorAll(".requests-table tbody tr");
        var found = false;
        
        rows.forEach(function(row) {
            var rowText = row.textContent.toLowerCase();
            if (rowText.includes(searchText)) {
                row.style.display = "";
                found = true;
            } else {
                row.style.display = "none";
            }
        });

        // Показываем или скрываем сообщение об отсутствии результатов
        if (found) {
            notFoundMessage.style.display = "none";
        } else {
            notFoundMessage.style.display = "block";
        }
    }
});
