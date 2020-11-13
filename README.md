# tb-profiler-webdriver

This repository hosts a lightweight python library to enable submission of data and retrieval of results from a tb-profiler webserver.
The library is currently only operational with the develpment version of `tb-profiler-webserver`. You can find test it out with http://bioinformatics.lshtm.ac.uk.

## Installation

```
git clone https://github.com/jodyphelan/tb-profiler-webdriver.git
cd tb-profiler-webdriver
python setup.py install
```

## Usage

```
import import tbprofiler_webdriver

# Create server object (default: host="https://localhost:5000")
server = tbprofiler_webdriver.tbprofiler_server()

# Send fastq files to be processed (default: platform="illumina")
run_id = server.send_fastq("sample_1.fastq.gz","sample_2.fastq.gz")

# Retrieve results
result = server.get_result(run_id)
```
