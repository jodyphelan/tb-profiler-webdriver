# tb-profiler-webdriver

This is a lightweight library to enable submission of data and retrieval of results from a tb-profiler webserver.

It is not fully functional right now and in development.

## Installation

```
git clone https://github.com/jodyphelan/tb-profiler-webdriver.git
cd tb-profiler-webdriver
python setup.py install
```

## Useage

```
import import tbprofiler_webdriver

server = tbprofiler_webdriver.tbprofiler_server()
run_id = server.send_fastq("sample_1.fastq.gz","sample_2.fastq.gz")
```
