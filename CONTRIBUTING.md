# Contributing

Want to help make this tool better? Awesome. I'm totally open to pull requests, bug reports, and new ideas.

## Found a bug?
If something breaks or your PC throws a weird error, open an issue! Just tell me what Windows version you're on and paste the error output so I can track it down.

## Got a new idea?
If you know of another safe Windows networking trick that I missed, open an issue and let's talk about it.

## Want to write some code?
If you want to add a new optimizer yourself, it's pretty straightforward:
1. Fork the repo and make your own branch from `master`.
2. Check out the `optimizers/` folder. All you have to do is create a new file, inherit from `BaseOptimizer`, and write your logic inside `apply_optimization()`.
3. Hook it up in `main.py`.
4. Submit a Pull Request.

Don't worry too much about strict formatting, just try to keep it readable and test it on your machine first. Thanks!
