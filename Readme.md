# PyCat 🐍

**A lightweight Python replacement for Netcat, built for networking and pentesting.**

PyCat is a simple command-line networking tool written in Python that provides basic Netcat-style functionality with a focus on keeping things lightweight and easy to understand.

> ⚠️ **For authorized security testing and educational purposes only.**
> Only scan or connect to systems you own or have explicit permission to test.

## ✨ Features

* 🔌 TCP client connections
* 👂 TCP listening mode
* 📡 Send messages to a target
* 🔎 Basic TCP port scanning
* ⚙️ Configurable target and port
* 🐍 Pure Python implementation
* 🪶 Lightweight and easy to modify

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/pycat.git
cd pycat
```

No external dependencies are required.

## 🚀 Usage

### Connect to a target

```bash
python3 pycat.py -t 127.0.0.1 -p 9999
```

PyCat will prompt you for a message to send.

### Listen for connections

```bash
python3 pycat.py -l -p 9999
```

The default port is `9999`.

### Port scanning

```bash
python3 pycat.py -s -t 127.0.0.1
```

PyCat will scan TCP ports from `1` through `65534` and report open ports.

## ⚙️ Arguments

| Argument         | Description                        |
| ---------------- | ---------------------------------- |
| `-l`, `--listen` | Start TCP listening mode           |
| `-p`, `--port`   | Specify the port (default: `9999`) |
| `-t`, `--target` | Specify the target IP/hostname     |
| `-s`, `--scan`   | Enable port scanning               |

## 🧪 Example

Start a listener:

```bash
python3 pycat.py -l -p 9999
```

Then from another machine or terminal:

```bash
python3 pycat.py -t 127.0.0.1 -p 9999
```

The listener accepts the connection, receives up to 4096 bytes, prints the received data, and responds with:

```text
Hello from the server!
```

## 🛠️ Built With

* **Python 3**
* `socket`
* `argparse`
* `sys`
* `datetime`

## 🎯 Why PyCat?

PyCat was created as a small, understandable alternative to Netcat for learning about:

* TCP sockets
* Client/server communication
* Port scanning
* Network programming
* Basic penetration-testing concepts

The goal is to keep the tool simple enough to understand while providing a foundation for future features.

## 🔮 Planned Features

Potential future improvements:

* Interactive shell mode
* UDP support
* Banner grabbing
* Improved scanning speed
* Service detection
* Timeout configuration
* Better error handling
* Multiple connection handling

## ⚠️ Disclaimer

PyCat is intended for **education, lab environments, CTFs, and authorized penetration testing**.

Do not use PyCat to scan, access, or interact with systems without permission. The author is not responsible for misuse of this software.

## 📄 License

Add your preferred open-source license to this repository.

