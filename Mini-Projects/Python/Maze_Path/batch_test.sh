for file in ./INPUT/*
do
  python ./SOURCE/maze.py -i $file -o "./OUTPUT/`basename "$file"`"
done