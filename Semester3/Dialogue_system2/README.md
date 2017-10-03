# Lab is based on TDM (Talkamatik company)

Go to lab.
Go to command line

### type next lines for running or test.
> tdm <br/>
> tdm buld<br/>
> tdm run eng<br/>


> Issue
- In case someone else is working on a DS2 lab and gets a "No module named funcsigs" error, here's a workaround:
- 1. Download and extract the tar.gz file from https://pypi.python.org/pypi/funcsigs.
- 2. Create/edit the file ~/.bash_profile and add:
- export PYTHONPATH=$PYTHONPATH:~/Downloads/funcsigs-1.0.2
- 3. Restart the terminal window.
- By Arild Metsän
