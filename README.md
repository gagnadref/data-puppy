data-puppy
==================

data-puppy is a simple HTTP log monitoring console program

##Running

Make sure you are using python 3.

You need to provide the absolute path to your access.log.

```bash
python datapuppy/LogMonitor.py absolute/path/to/your/access.log
```

##Test with a HTTP log generator

You can test the program without any access.log file, using a HTTP log generator.

```bash
python test/TestLogMonitor.py
```

##Next improvements to be added

* Display the evolution of the metrics
* Use a log file on a remote server (via a socket)
* Monitor several websites in the same console
* Save the metrics and the alerts in a database for other uses (web app,...)
* Clean the history on demand
