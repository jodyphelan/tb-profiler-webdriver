import requests

class tbprofiler_server:
    def __init__(self,host="http://localhost:5000"):
        self.host = host
    def send_fastq(self,fq1,fq2):
        files = {
            "file1":open("/home/jody/tbprofiler_test_data/por5A1_1.fastq.gz","rb"),
            "file2":open("/home/jody/tbprofiler_test_data/por5A1_2.fastq.gz","rb")
        }
        data = {"platform":"illumina","single_sample_submit":""}
        print("%(host)s/upload" % vars(self),files,data)
        r = requests.post("%(host)s/upload" % vars(self),files=files,data=data)

        return r.url.split("/")[-1]

    def check_results(self,id):
        return requests.get(self.host+"/results/"+id).content
