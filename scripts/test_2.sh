eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -xe

python src/s1.py & 
sleep 0.5

python src/c1.py &
python src/c1.py &
python src/c1.py &
python src/c1.py &
python src/c1.py &
python src/c1.py

sleep 5
