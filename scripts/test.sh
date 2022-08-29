eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -xe

# Check all syntax errors
python -m compileall src

# Start server
python src/s1.py & 
sleep 0.5

# Start client
python src/c1.py &
sleep 5

# Start client2, qps should increase
python src/c1.py &
sleep 5

python src/c1.py &
sleep 5
