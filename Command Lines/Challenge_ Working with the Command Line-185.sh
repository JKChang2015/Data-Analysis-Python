## 1. Command Line Python ##


cd ..
cd ~
pwd

## 2. Creating a script ##


echo -e 'import sys\n\nif __name__ == "__main__":\n    print(sys.argv[1])' > script.py

## 3. Change file permissions ##


chmod 0700 script.py

## 4. Create a virtualenv ##


virtualenv -p /usr/bin/python3 script
source script/bin/activate

## 5. Move the script ##


mkdir printer
mv script.py printer

## 6. Execute the script ##


cd printer
python script.py "I'm so good at challenges!"