-- ТЕСТОВЫЕ ДАННЫЕ:
insert into clients values
(1, 'Иванов Иван Сергеевич', 45000, 18000, 'VIP', 740),
(2, 'Смирнова Мария Викторовна', 3000, 18000, 'Обычный', 520),
(3, 'Кузнецов Андрей Петрович', 25000, 8000, 'Премиум', 680),
(4, 'Новиков Сергей Иванович', 20000, 10000, 'Заблокирован', 300),
(5, 'Петрова Ольга Алексеевна', 4000, 20000, 'Обычный', 450),
(6, 'Федоров Николай Павлович', 48000, 15000, 'VIP', 710);


select
    id,
    category,
    balance,
    debt
from clients
where balance > 40000 and category = 'VIP'
order by balance desc
limit 10;

insert into clients (id, name, balance, debt, category, credit_score) values (
    100, 'Тестовый Клиент', 50000, 0, 'VIP', 800
);
