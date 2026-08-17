from services.task_service import (
    create_task,
    delete_task,
    update_task,
    search_task
)


def test_create_task(monkeypatch):
    tasks = []

    def fake_save():
        pass

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "Изучить Python"
    )

    create_task(tasks, fake_save)

    assert len(tasks) == 1
    assert tasks[0] == "Изучить Python"


def test_delete_task(monkeypatch):
    tasks = ["Python", "Docker"]

    def fake_save():
        pass

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    delete_task(tasks, fake_save)

    assert len(tasks) == 1
    assert tasks[0] == "Docker"


def test_update_task(monkeypatch):
    tasks = ["Python", "Docker"]

    def fake_save():
        pass

    inputs = iter(["2", "FastAPI"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    update_task(tasks, fake_save)

    assert len(tasks) == 2
    assert tasks[1] == "FastAPI"


def test_search_task(monkeypatch, capsys):
    tasks = ["Изучить Python", "Сделать Docker", "Изучить Git"]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "Python"
    )

    search_task(tasks)

    captured = capsys.readouterr()

    assert "Изучить Python" in captured.out


def test_delete_task_invalid_number(monkeypatch, capsys):
    tasks = ["Python", "Docker"]

    def fake_save():
        pass

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "999"
    )

    delete_task(tasks, fake_save)

    captured = capsys.readouterr()

    assert "Такой задачи нет!" in captured.out
    assert len(tasks) == 2
    
    
def test_delete_task_invalid_input(monkeypatch, capsys):
    tasks = ["Python", "Docker"]

    def fake_save():
        pass

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "abc"
    )

    delete_task(tasks, fake_save)

    captured = capsys.readouterr()

    assert "Нужно ввести число!" in captured.out
    assert len(tasks) == 2