class ContextManager:
    level = 0
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        ContextManager.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ContextManager.level -= 1

    def write(self, text: str):
        with open(self.filename, "a") as f:
            f.write(" " * ContextManager.level + text + "\n")

with ContextManager("output.txt") as writer:
    writer.write("Первый уровень")
    with writer:
        writer.write("Второй уровень")
        with writer:
            writer.write("Третий уровень")
    writer.write("Снова первый")
