from app import db, app  # Импортируем приложение и базу данных

with app.app_context():
    db.create_all()  # Создаёт все таблицы, определённые в моделях
    print("База данных успешно инициализирована.")
