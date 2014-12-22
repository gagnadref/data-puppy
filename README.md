data-puppy
==================

data-puppy is a simple HTTP log monitoring console program

##Running

Make sure you are using python 3.

You need to provide the absolute path of you access.log.

```bash
python datapuppy/LogMonitor.py absolute/path/access.log
```

##Test with a HTTP log generator

You can test the program without any access.log file, using a HTTP log generator.

```bash
python test/TestLogMonitor.py
```

##Next improvement to be added

* Displaying the evolution of the metrics
* Using a log file on a remote server (via a socket)
* Monitoring several websites in the same console
* Saving the metrics and the alerts in a database for other uses (web app,...)
