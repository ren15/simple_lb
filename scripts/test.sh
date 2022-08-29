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

# Start client3, qps should increase
python src/c1.py &
sleep 5


# Start client4..10, qps should increase
for i in {4..10}
do
    python src/c1.py &
done

sleep 5

