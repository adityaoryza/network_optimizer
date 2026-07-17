# Windows Network Optimizer

A premium Python-based Command-Line Interface (CLI) tool designed to optimize Windows networking parameters for lower latency, reduced packet loss, and better throughput.

## Features
- **DNS Cache Optimizer:** Flushes outdated DNS entries to resolve connection hangs.
- **TCP Auto-Tuning:** Ensures Windows dynamically adjusts the receive window size for maximum download speeds.
- **TCP ECN Capability:** Enables Explicit Congestion Notification to prevent packet loss and lag spikes during heavy traffic.
- **Ping Benchmark:** Automatically measures latency before and after the optimization process to show real-time improvements.
- **Auto-Elevation:** Automatically requests Windows Administrator privileges if run without them (via UAC).
- **Premium CLI UI:** Features a beautifully styled terminal output with ASCII banners and ANSI colored logs.

## Requirements
- Windows 10 or Windows 11
- Python 3.6+

## Installation
Clone this repository and navigate into the directory:

```bash
git clone https://github.com/adityaoryza/network_optimizer.git
cd network_optimizer
```

*(No external pip dependencies required. Built entirely with Python's standard library).*

## Usage
Simply run `main.py` using Python. The tool will automatically request Administrator privileges.

```bash
python main.py
```

## Architecture
This project follows Enterprise-level architecture using SOLID principles, Dependency Injection, and the Strategy pattern for optimizers.

```text
network_optimizer/
├── core/             # Execution and exception handling
├── optimizers/       # Individual optimization strategies (DNS, TCP, etc.)
├── benchmarks/       # Network latency measuring tools
├── utils/            # Privilege checking and CLI styling
└── main.py           # Application Entrypoint & Orchestrator
```
