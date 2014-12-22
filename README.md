data-puppy
==================

data-puppy is a simple HTTP log monitoring console program

##Running

Make sure you are using python 3
You need to provide the absolute path of you access.log

```bash
python datapuppy/LogMonitor.py absolute/path/access.log
```

##Test with a HTTP log generator

You can test the program without any access.log file, using a HTTP log generator

```bash
python test/TestLogMonitor.py
```
