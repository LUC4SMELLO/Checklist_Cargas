# Documentação – Classe DBMonitor

## Objetivo

A classe DBMonitor é responsável por monitorar mudanças em um banco SQLite e executar uma função (callback) quando alguma alteração for detectada.

Ela foi projetada para funcionar sem travar a interface do Tkinter, utilizando:

- thread separada para monitoramento do banco

- fila (queue) para comunicação entre threads

- after() do Tkinter para executar código com segurança na thread da interface

## Estratégia utilizada

O monitoramento do banco é feito utilizando:
```
PRAGMA data_version
```
Esse comando do SQLite retorna um número que muda sempre que o banco é modificado por outra conexão.

**Fluxo geral:**
```
Thread separada
      ↓
Consulta PRAGMA data_version
      ↓
Detecta mudança
      ↓
Coloca evento na queue
      ↓ 
Tkinter processa a queue
      ↓
O Callback é executado na thread da interface
```
Isso evita problemas como:

- Travamento da interface
- Acesso inseguro ao Tkinter por threads
- Polling pesado do banco

## Estrutura da Classe
### Construtor
```python
def __init__(self, db_path, callback, tk_root, interval=0.5)
```

Inicializa o monitor do banco de dados.

### Parâmetros

---
**db_path**
Caminho do arquivo do banco SQLite.

Exemplo:
```python
Path("database/app.db")
```

---

**callback**
Função executada quando uma alteração no banco é detectada.

Exemplo:
```python
def atualizar_interface():
    carregar_dados()
```

---
**tk_root**
Janela principal do Tkinter.

Usado para agendar execuções com:
```python
root.after()
```
Isso garante que o callback execute na thread da interface.

---
**interval**

Intervalo (em segundos) entre verificações do banco.

Valor padrão:
```
0.5 segundos
```
Isso significa:
```
2 verificações por segundo
```

## Atributos importantes
**ignore_until**
```python
self.ignore_until = 0
```

Usado para ignorar temporariamente mudanças no banco.

Isso evita que o sistema reaja a alterações feitas pela própria aplicação.

---
**q**
```python
self.q = queue.Queue()
```

Fila usada para comunicação entre:

```
Thread de monitoramento
        ↓
Thread do Tkinter
```
Threads não devem chamar Tkinter diretamente.

---
**stop_event**
```python
self.stop_event = threading.Event()
```
Evento usado para parar a thread de monitoramento com segurança.

---
**thread**
```python
self.thread = threading.Thread(target=self._worker, daemon=True)
```

Thread responsável por:

- consultar o banco
- detectar mudanças
- enviar eventos para a queue

```daemon=True``` significa que a thread encerra automaticamente quando o programa fecha.

## Métodos públicos

**start()**
```python
def start(self):
```
Inicia o monitoramento do banco.

Passos executados:

**1º inicia a thread de monitoramento**
```python
self.thread.start()
```

**2º inicia o loop de processamento da fila**

```python
self.root.after(200, self._process_queue)
```
Esse loop roda na thread do Tkinter.

---
**stop()**
```python
def stop(self):
```
Para o monitoramento.

Passos:

**1º sinaliza para a thread parar**
```python
self.stop_event.set()
```

**2º aguarda o encerramento da thread**
```python
self.thread.join(timeout=1)
```

---
**ignore_next()**
```python
def ignore_next(self, seconds=1)
```
Ignora mudanças no banco por alguns segundos.

Usado quando a própria aplicação altera o banco, evitando disparar o callback.

Exemplo de uso:
```python
monitor.ignore_next()

model.inserir_dados()
```
Assim a alteração não dispara atualização desnecessária.

## Métodos internos

Métodos internos começam com _ porque não devem ser usados fora da classe.

**_worker()**

Thread responsável por monitorar o banco.

Fluxo:

### 1º Abre conexão SQLite
```python
sqlite3.connect(check_same_thread=False)
```

```check_same_thread=False``` permite que a conexão SQLite seja usada dentro da thread criada.


### 2º Lê versão inicial do banco
```python
PRAGMA data_version
```

Essa será a referência inicial.

### 3º Loop de monitoramento

Executa continuamente até ```stop_event``` ser ativado.

Passos do loop:

1º consulta novamente ```data_version```

2º compara com a versão anterior
```python
if v != last
```

3º se mudou:

atualiza ```last```

verifica se não está no período de ignorar

4º se permitido:

coloca evento na fila
```python
self.q.put("db_changed")
```

### 4º Intervalo entre verificações
```python
time.sleep(self.interval)
```
Isso evita consumo excessivo de CPU.

### 5º Encerramento seguro

A conexão é fechada no ```finally.```

---
**_process_queue()**

Executa na thread do Tkinter.

Responsável por:

- ler eventos da fila
- executar callbacks

Fluxo:

### 1º tenta ler todos eventos disponíveis
```python
self.q.get_nowait()
```

Se a fila estiver vazia:

```python
queue.Empty
```
é capturado.

### 2º se o evento for "db_changed"

executa:
```python
self.callback()
```

Esse callback agora roda na thread da interface, o que é seguro para Tkinter.

### 3º agenda próxima execução
```python
self.root.after(200, self._process_queue)
```

Isso cria um loop periódico que processa os eventos da fila.

# Resumo do fluxo completo
```
DBMonitor.start()
        ↓
Thread _worker inicia
        ↓
PRAGMA data_version
        ↓
detecta mudança no banco
        ↓
coloca evento na queue
        ↓
_process_queue roda no Tkinter
        ↓
callback é executado
        ↓
interface atualiza
```

Vantagens dessa implementação

- Não trava a interface
- Thread-safe para Tkinter
- Detecta mudanças feitas por outras máquinas
- Baixo consumo de CPU
- Fácil de integrar com MVC