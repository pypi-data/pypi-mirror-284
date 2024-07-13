python -m venv .venv

source .venv/Scripts/activate
pip install maturin
// mkdir chatlogger_core // not working
maturin init
// maturin new chatlogger_core
// cd chatlogger_core
maturin develop


source deactivate


