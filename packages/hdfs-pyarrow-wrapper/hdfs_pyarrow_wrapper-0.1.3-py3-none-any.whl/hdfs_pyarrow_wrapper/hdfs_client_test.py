# fs.chunk_files("/tmp/stack", "1.text", "2.text")
import hashlib

from hdfs_utils import hdfs_utils as fs

path = "/tmp/hdfs-demo"
subdir = path + "/subdir0/"

print(f"start create dir {subdir}")
fs.get_hdfs_client().create_dir(subdir)

print(f"copy files to sub dir {subdir}")
fs.get_hdfs_client().copy_file(path + "/file0.txt", subdir + "/file0.txt")

print(f"list path {path}")
filesInfo = fs.ls(path)
for fi in filesInfo:
    print("FileInfo:", fi)

print(f"exist {path} start")
exist = fs.exists(path)

if exist:
    print("File exists ", path)
else:
    print("File does not exist ", path)

print(f"count files recursively in {path}")
cnt = fs.count_files_recursive(path)

print(f"Count in {path} {cnt}")

print(f"delete file {subdir} + file0.txt")
fs.get_hdfs_client().delete_file(path + "/subdir0/file0.txt")

for name, content in fs.ChunkFileIterator("/tmp/test-fuse/stack2"):
    with open("./output_files/" + name, 'rb') as f:
        print(name, len(content), hashlib.md5(content).hexdigest() == hashlib.md5(f.read()).hexdigest())
