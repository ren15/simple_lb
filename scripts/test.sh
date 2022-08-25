eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"
python -m compileall src
python src/s1.py & 
sleep 0.5
python src/c1.py &
python src/c1.py