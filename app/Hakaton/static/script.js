// script.js

// Получаем ссылку на форму входа
const loginForm = document.getElementById('login-form');

// Добавляем обработчик события на отправку формы
loginForm.addEventListener('submit', function(event) {
    // Предотвращаем стандартное поведение формы (перезагрузка страницы)
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => {
        if (response.ok) {
            // Переход на страницу работника компании
            window.location.href = '/emp'; // Обращение к эндпоинту /employee
        } else {
            alert('Логин или пароль неверны');
        }
    })
    .catch(error => {
        console.error('Ошибка при проверке логина:', error);
    });
});
