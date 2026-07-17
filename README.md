# Windows Network Optimizer

Hey there! 👋 I built this Python CLI tool because I was tired of manually dealing with Windows network issues and lag spikes. This script optimizes your network settings to lower latency, reduce packet loss, and boost your download speeds. 

No sketchy registry hacks—just standard, safe Windows commands automated for you.

## What it does
- **Flushes DNS:** Clears out old connection data so your browser and games connect faster.
- **Tunes TCP Auto-Tuning:** Sets Windows to dynamically adjust your receive window (essential for maxing out your download speeds).
- **Enables TCP ECN:** Tells your router to play nice during heavy traffic instead of just dropping packets (which causes those annoying lag spikes in games).
- **Built-in Ping Test:** Pings Cloudflare (1.1.1.1) before and after running so you can actually see the difference.

## What you need
- Windows 10 or 11
- Python 3.6+

## How to use it
Just clone the repo and run the script. It's built entirely using Python's standard library, so you don't even need to run `pip install` for anything.

```bash
git clone https://github.com/adityaoryza/network_optimizer.git
cd network_optimizer
python main.py
```
*Note: The script will automatically ask for Administrator permissions when you run it (it needs them to change TCP settings).*

## Under the hood
I built this using solid OOP principles and the Strategy Pattern. If you want to dive into the code:
- `core/`: Where the system commands get executed safely.
- `optimizers/`: The actual optimization modules (feel free to add your own).
- `benchmarks/`: The ping testing logic.
- `main.py`: The entrypoint that brings it all together.

Hit me up or open an issue if you have ideas for more features!
