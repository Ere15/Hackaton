document.addEventListener("DOMContentLoaded", function() {
    console.log('Скрипт был успешно выполнен!');
    // Отправляем GET-запрос на эндпоинт для получения данных
    fetch('/owner/requests/pending')
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при получении данных');
            }
            return response.json();
        })
        .then(data => {
            // Обновляем таблицу с данными
            updateTable(data);
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });

    function updateTable(data) {
        const tbody = document.querySelector('.requests-table tbody');
        tbody.innerHTML = ''; // Очищаем содержимое tbody

        // Проходим по данным и добавляем строки в таблицу
        data.forEach(request => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${request.id}</td>
                <td>${request.name}</td>
                <td>${request.label}</td>
                <td>${request.status}</td>
                <td>${request.date}</td>
            `;
            tbody.appendChild(row);
        });
    }
});
