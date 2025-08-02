apt update
apt install -y curl
apt install -y git


curl -sSL https://install.python-poetry.org | python3 -
apt install -y build-essential


# パスを通す
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
# 追記後、ファイルを読み込み直す
source ~/.bashrc


poetry install --no-root