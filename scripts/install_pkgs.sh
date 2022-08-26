set -xe

wget -q -c https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -b

curl -sfL https://get.k3s.io | sh -
