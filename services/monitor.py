import sqlite3
import threading
import queue
import time


class DBMonitor:
    def __init__(self, db_path, callback, tk_root, interval=0.5):
        """
        Monitora um banco de dados.

        Paremeters
        ----------
            db_path
                Caminho do banco de dados.
            callback
                Função chamada quando o banco de dados mudar.
            tk_root
                Janela tkinter (para usar after).
            interval
                Intervalo de verificação.
        """
        self.db_path = db_path
        self.callback = callback
        self.root = tk_root
        self.interval = interval
        self.ignore_until = 0

        self.q = queue.Queue()
        self.stop_event = threading.Event()

        self.thread = threading.Thread(
            target=self._worker,
            daemon=True
        )

    def start(self):
        self.thread.start()
        self.root.after(200, self._process_queue)

    def stop(self):
        self.stop_event.set()
        self.thread.join(timeout=1)
    
    def ignore_next(self, seconds=1):
        self.ignore_until = time.time() + seconds

    def _worker(self):
        conexao = sqlite3.connect(str(self.db_path), check_same_thread=False)
        cursor = conexao.cursor()

        cursor.execute("PRAGMA data_version")
        last = cursor.fetchone()[0]

        try:
            while not self.stop_event.is_set():

                cursor.execute("PRAGMA data_version")
                v = cursor.fetchone()[0]

                if v != last:
                    last = v
                    
                    if time.time() > self.ignore_until:
                        self.q.put("db_changed")

                time.sleep(self.interval)

        finally:
            conexao.close()

    def _process_queue(self):
        try:
            while True:
                item = self.q.get_nowait()

                if item == "db_changed":
                    self.callback()

        except queue.Empty:
            pass

        self.root.after(200, self._process_queue)
