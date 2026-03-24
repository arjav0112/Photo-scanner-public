# Contributing to Photo Scanner

Thank you for your interest in Photo Scanner! While the core AI engines and scoring algorithms are proprietary, we value community feedback and engagement.

## How to Contribute

### 1. Feature Requests & Ideas
If you have an idea for a new analysis module or search capability, please [open an issue](https://github.com/arjavjain5203/photo-scanner-public/issues). We are actively building the Q2/Q3 roadmap.

### 2. Bug Reports
Found a scanning issue or unexpected search behavior? Help us improve by filing a detailed bug report with:
- Your Python version and OS
- The command you ran
- The error output or unexpected behavior

### 3. Documentation
Found a typo in our README or want to improve the public API documentation? PRs are welcome for the `docs/` folder.

## Development Setup

Since this is a teaser repo, you can explore the architecture but the engines operate in "stub mode" — returning placeholder results.

```bash
# Clone the repo
git clone https://github.com/arjavjain5203/photo-scanner-public.git
cd photo-scanner-public

# Install dependencies (Poetry)
pip install poetry
poetry install

# Run the CLI (stub mode)
python main.py scan ./your-photos
python main.py search "sunset beach"
```

## Security Reporting
If you find a security vulnerability, please do NOT open a public issue. Refer to our [SECURITY.md](SECURITY.md) for private reporting instructions.

---
*Happy scanning!*
