import requests
import json

class tbprofiler_server:
    def __init__(self,host="http://localhost:5000"):
        self.host = host
    def send_fastq(self,fq1,fq2):
        files = {
            "file1":open(fq1,"rb"),
            "file2":open(fq2,"rb")
        }
        data = {"platform":"illumina","single_sample_submit":""}
        print("%(host)s/upload" % vars(self),files,data)
        r = requests.post("%(host)s/upload" % vars(self),files=files,data=data)

        return r.url.split("/")[-1]

    def get_result(self,id):
        return json.loads(requests.get(self.host+"/results/json/"+id).content)
