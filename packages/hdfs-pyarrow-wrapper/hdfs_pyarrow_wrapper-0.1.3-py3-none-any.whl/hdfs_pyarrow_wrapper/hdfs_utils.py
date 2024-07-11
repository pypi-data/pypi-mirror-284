# Ensure the script is run with Python 3.7 or later
import json
import os
import random
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
import pyarrow.fs as fs

DEFAULT_BUFFER_SIZE = 64 * 1024

_LOCAL_FS = fs.LocalFileSystem()

class HDFSClientSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._hdfs_client = fs.HadoopFileSystem(host='default', port=8020)
        return cls._instance

    @property
    def client(self):
        return self._instance._hdfs_client


def get_hdfs_client():
    return HDFSClientSingleton().client


def upload_file_to_hdfs(hdfs_client, local_path, hdfs_path, check_exists):
    try:
        if check_exists:
            try:
                file_info = hdfs_client.get_file_info(hdfs_path)
                if file_info.type != fs.FileType.NotFound:
                    print(f"File {hdfs_path} already exists. Skipping upload.")
                    return True
            except Exception as e:
                print(f"Error checking file info for {hdfs_path}: {e}")

        with open(local_path, 'rb') as local_file:
            with hdfs_client.open_output_stream(hdfs_path) as hdfs_file:
                hdfs_file.upload(local_file, DEFAULT_BUFFER_SIZE)

        print(f"Successfully uploaded {local_path} to {hdfs_path}")
        return True
    except Exception as e:
        print(f"Error uploading {local_path} to {hdfs_path}: {e}")
        return False, local_path, str(e)


def download_file_from_hdfs(hdfs_client, hdfs_path, local_path):
    try:
        with hdfs_client.open_input_file(hdfs_path) as hdfs_file:
            hdfs_file.download(local_path, DEFAULT_BUFFER_SIZE)
        if os.path.exists(local_path):
            print(f"Successfully downloaded {hdfs_path} to {local_path}")
            return True
        else:
            print(f"Error downloading {hdfs_path} to {local_path}")
            return False
    except Exception as e:
        print(f"Error downloading {hdfs_path} to {local_path}: {e}")
        return False, hdfs_path, str(e)


def multithreaded_upload(files_mapping, check_exists=False, max_workers=4):
    hdfs_client = HDFSClientSingleton().client
    start_time = time.time()
    success_count = 0
    fail_count = 0
    failed_files = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(upload_file_to_hdfs, hdfs_client, local_path, hdfs_path, check_exists): (
            local_path, hdfs_path)
            for local_path, hdfs_path in files_mapping.items()}
        for future in as_completed(future_to_file):
            local_path, hdfs_path = future_to_file[future]
            try:
                result = future.result()
                if result is True:
                    success_count += 1
                else:
                    fail_count += 1
                    failed_files.append(result)
            except Exception as e:
                fail_count += 1
                failed_files.append((local_path, str(e)))

    end_time = time.time()
    total_time_ms = (end_time - start_time) * 1000

    print(f"Upload completed in {total_time_ms:.2f} ms.")
    print(f"Total files prepared for upload: {len(files_mapping)}")
    print(f"Success: {success_count}")
    print(f"Fail: {fail_count}")
    if failed_files:
        print("Failed files and error messages:")
        for file, error in failed_files:
            print(f"{file}: {error}")


def multithreaded_download(files_mapping, max_workers=4):
    hdfs_client = HDFSClientSingleton().client
    start_time = time.time()
    success_count = 0
    fail_count = 0
    failed_files = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {
            executor.submit(download_file_from_hdfs, hdfs_client, hdfs_path, local_path): (local_path, hdfs_path)
            for hdfs_path, local_path in files_mapping.items()}
        for future in as_completed(future_to_file):
            local_path, hdfs_path = future_to_file[future]
            try:
                result = future.result()
                if result is True:
                    success_count += 1
                else:
                    fail_count += 1
                    failed_files.append(result)
            except Exception as e:
                fail_count += 1
                failed_files.append((hdfs_path, str(e)))

    end_time = time.time()
    total_time_ms = (end_time - start_time) * 1000

    print(f"Download completed in {total_time_ms:.2f} ms.")
    print(f"Total files prepared for download: {len(files_mapping)}")
    print(f"Success: {success_count}")
    print(f"Fail: {fail_count}")
    if failed_files:
        print("Failed files and error messages:")
        for file, error in failed_files:
            print(f"{file}: {error}")


def prepare_files(dir_path, num_files=100, max_size_mb=128):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for i in range(num_files):
        file_size = random.randint(0, max_size_mb * 1024 * 1024)  # size in bytes
        file_path = os.path.join(dir_path, f"file{i}.txt")
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))
    print(f"Prepared {num_files} files in {dir_path}")


# change from list to ls, avoid key word conflicts in python
def ls(dir_path, recursive=False):
    hdfs_client = HDFSClientSingleton().client
    f_info = hdfs_client.get_file_info(dir_path)
    if f_info.type == fs.FileType.Directory:
        return hdfs_client.get_file_info(fs.FileSelector(dir_path, recursive))
    elif f_info.type == fs.FileType.File:
        return [f_info]
    else:
        return []


def exists(path):
    if path is None:
        return False
    hdfs_client = HDFSClientSingleton().client
    f_info = hdfs_client.get_file_info(path)
    return f_info.type != fs.FileType.NotFound


def count_files_recursive(dir_path):
    f_cnt = 0
    for f in list(dir_path):
        if f.type == fs.FileType.File:
            f_cnt += 1
    return f_cnt


STACKED_SIGNATURE = b'00CHUNK'
SIGNATURE_LENGTH = len(STACKED_SIGNATURE)
META_LENGTH_SIZE = 4  # 4 bytes to store the length of metadata

_HDFSIMPL_STR = 'HDFS'
_FUSEIMPL_STR = 'LOCAL'

CHUNK_FILE_WRITE_FSIMPL = os.getenv('CHUNK_FILE_WRITE_FSIMPL', _HDFSIMPL_STR)
CHUNK_FILE_READ_FSIMPL = os.getenv('CHUNK_FILE_READ_FSIMPL', _FUSEIMPL_STR)


def _get_CHUNK_FILE_READ_FSIMPL():
    """
    根据环境变量的设置，使用不同的FileSystem实现来读取chunk文件
    :return: pyarrow FileSystem
    """
    # Open the output file in binary write mode
    chunk_file_fs = None
    if CHUNK_FILE_READ_FSIMPL == _HDFSIMPL_STR:
        chunk_file_fs = get_hdfs_client()
    else:
        chunk_file_fs = _LOCAL_FS
    return chunk_file_fs


def chunk_files(output_file, *input_files):
    # Dictionary to store metadata
    meta_data = {}
    current_position = 0

    # Open the output file in binary write mode
    if CHUNK_FILE_WRITE_FSIMPL == _HDFSIMPL_STR:
        chunk_file_fs = get_hdfs_client()
    else:
        chunk_file_fs = _LOCAL_FS

    with chunk_file_fs.open_output_stream(output_file) as out_f:
        # Loop through each input file
        for file_path in input_files:
            # Get the size of the input file
            file_size = os.path.getsize(file_path)
            # Write the content of the input file to the output file
            with open(file_path, 'rb') as in_f:
                content = in_f.read()
                out_f.write(content)

            # Add metadata information
            meta_data[os.path.basename(file_path)] = {
                'off': current_position,
                'len': file_size
            }
            current_position += file_size

        # Convert metadata to JSON and get its length
        meta_json = json.dumps(meta_data)
        meta_bytes = meta_json.encode('utf-8')
        meta_length = len(meta_bytes)

        # Write the metadata, its length, and the signature to the output file
        out_f.write(meta_bytes)
        out_f.write(meta_length.to_bytes(META_LENGTH_SIZE, byteorder='big'))
        out_f.write(STACKED_SIGNATURE)


def _read_meta_data(f):
    f.seek(-SIGNATURE_LENGTH, os.SEEK_END)
    signature = f.read(SIGNATURE_LENGTH)

    if signature != STACKED_SIGNATURE:
        raise ValueError("File format is not a chunk format.")

    f.seek(-SIGNATURE_LENGTH - META_LENGTH_SIZE, os.SEEK_END)
    meta_length_bytes = f.read(META_LENGTH_SIZE)
    meta_length = int.from_bytes(meta_length_bytes, byteorder='big')

    f.seek(-SIGNATURE_LENGTH - META_LENGTH_SIZE - meta_length, os.SEEK_END)
    meta_bytes = f.read(meta_length)

    meta_json = meta_bytes.decode('utf-8')
    meta_data = json.loads(meta_json)

    return meta_data


def read_chunk_file_meta(chunk_file):
    """
    读取chunk文件的meta信息，默认是读本读路径（fuse路径挂载方式同样支持）
    export CHUNK_FILE_READ_FSIMPL='LOCAL'为默认值，修改为CHUNK_FILE_READ_FSIMPL='HDFS'可从HDFS读取
    :param chunk_file: chunk方式写入的文件
    :return: chunk_file中的meta信息，包括包含的文件名与offset、length
    """
    with _get_CHUNK_FILE_READ_FSIMPL().open_input_file(chunk_file) as f:
        meta_data = _read_meta_data(f)
        return meta_data


def read_chunk_file_meta_from_hdfs(chunk_file):
    """
    与read_chunk_file_meta功能一致，但是强制使用hdfs读取
    :param chunk_file:
    :return:
    """
    return _read_chunk_file_meta(chunk_file, get_hdfs_client())


def read_chunk_file_meta_from_local(chunk_file):
    """
    与read_chunk_file_meta功能一致，但是强制使用LocalFileSystem读取
    :param chunk_file:
    :return:
    """
    return _read_chunk_file_meta(chunk_file, _LOCAL_FS)


def _read_chunk_file_meta(chunk_file, f):
    """
    读取chunk文件的meta信息
    :param chunk_file: chunk方式写入的文件
    :return: chunk_file中的meta信息，包括包含的文件名与offset、length
    """
    with f.open_input_file(chunk_file) as f:
        meta_data = _read_meta_data(f)
        return meta_data


def read_files_in_chunk(chunk_file, *filenames):
    """
    根据filesnames读取chunk_file
    :param chunk_file: chunk_file的路径
    :param filenames:
    :return:
    """
    return _read_files_in_chunk(chunk_file, _get_CHUNK_FILE_READ_FSIMPL(), *filenames)


def read_files_in_chunk_from_hdfs(chunk_file, *filenames):
    """
   根据filesnames读取chunk_file, 从HDFS读取
   :param chunk_file: chunk_file的路径
   :param filenames:
   :return:
   """
    return _read_files_in_chunk(chunk_file, get_hdfs_client(), *filenames)


def read_files_in_chunk_from_local(chunk_file, *filenames):
    """
    根据filesnames读取chunk_file, 从Local读取
    :param chunk_file:
    :param filenames:
    :return:
    """
    return _read_files_in_chunk(chunk_file, _LOCAL_FS, *filenames)


def _read_files_in_chunk(chunk_file, f, *filenames):
    """
    根据filesnames读取chunk_file
    :param chunk_file: chunk_file的路径
    :param filenames:
    :return:
    """
    result = {}
    with f.open_input_file(chunk_file) as f:
        meta_data = _read_meta_data(f)
        for filename in filenames:
            if filename in meta_data:
                offset = meta_data[filename]['off']
                length = meta_data[filename]['len']
                f.seek(offset)
                content = f.read(length)
                result[filename] = {'content': content, 'length': length}
            else:
                result[filename] = {'content': None, 'length': 0}

        return result


CHUNK_FILE_SUFFIX = '.chunk'
CHUNK_FILE_PREFIX = "chunk_"


# chunk files APIs
def upload_dir_chunk(dir_path, dest_path, file_filter_func=None, concat_max_size=256, file_max_size_to_merge=128,
                     max_workers=4):
    """
    upload_dir_chunk方法使用以下技术做上传优化
    1. 合并小于file_max_size_to_merge=128MB的文件到一个大文件，并且为该大文件生成一个索引文件
    2. 通过计算本地文件大小，多线程上传文件，最大线程数为max_workers
    3. 自动生成文件名，以'chunk_'开头，以'.chunk'结尾
    :param dir_path: 本地路径
    :param dest_path: HDFS路径
    :param file_filter_func: 上传路径过滤器，为lambad表达式
    :param concat_max_size: 合并后文件大小的上限，默认为256MB
    :param file_max_size_to_merge: 本地文件合并的阈值上限，小于该值的会进行合并，默认为128MB
    :param max_workers: 多线程上传的最大线程数，默认为4
    :return: index文件的数组
    """
    if not os.path.isdir(dir_path):
        return None

    if not dest_path.endswith("/"):
        dest_path += "/"

    files_to_upload = {}
    files_with_size = []

    concat_max_size = concat_max_size * 1024 * 1024
    file_max_size_to_merge = file_max_size_to_merge * 1024 * 1024

    # 根据file_filter_func进行过滤
    for dirpath, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if file_filter_func and not file_filter_func(filename):
                continue
            filepath = os.path.join(dirpath, filename)
            filesize = os.path.getsize(filepath)
            if filesize > file_max_size_to_merge:
                files_to_upload[filepath] = dest_path + filename
            else:
                files_with_size.append((dirpath + '/' + filename, filesize))

    # start upload files with file size under file_max_size_to_merge
    if files_to_upload:
        print(f'Directly uploading {len(files_to_upload)} files')
        fs.multithreaded_upload(files_to_upload, max_workers=max_workers)

    # partition files with size
    groups = _partition_files(files_with_size, concat_max_size)
    print(f'Generate {len(groups)} groups')
    _submit_groups_to_executors(groups, dest_path, max_workers)


# upload groups file to hdfs using merge
def _submit_groups_to_executors(groups, dest_dir, max_worker):
    with ThreadPoolExecutor(max_workers=max_worker) as executor:
        futures = []
        for i, group in enumerate(groups):
            group_id = uuid.uuid4()
            local_files = [file for file, _ in group]
            output_file = f"{dest_dir}/{CHUNK_FILE_PREFIX}{group_id}_{i + 1}{CHUNK_FILE_SUFFIX}"
            futures.append(executor.submit(chunk_files, output_file, *local_files))
        # Wait for all futures to complete
        for future in futures:
            future.result()


def _partition_files(files_with_size, max_size):  # 256MB in bytes
    groups = []
    current_group = []
    current_group_size = 0

    for filename, filesize in files_with_size:
        if current_group_size + filesize <= max_size:
            current_group.append((filename, filesize))
            current_group_size += filesize
        else:
            groups.append(current_group)
            current_group = [(filename, filesize)]
            current_group_size = filesize

    if current_group:
        groups.append(current_group)

    return groups


class ChunkFileIterator:
    """
    Based on chunk file format, user can iterate over the origin file by calling StackFileIterator(chunk_file)

    example:
    for file_name, file_content_in_bytes in StackFileIterator(chunk_file):
        print(file_name + ":" + file_content_in_bytes)
    """

    def __init__(self, chunk_file):
        self.chunk_file = chunk_file
        self.current = 0
        self.meta = read_chunk_file_meta(chunk_file)
        self.fs_stream = _get_CHUNK_FILE_READ_FSIMPL().open_input_file(chunk_file)

        self.filenames = sorted(self.meta.keys(), key=lambda k: self.meta[k]['off'])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.filenames):
            curr_f_name = self.filenames[self.index]
            self.index += 1
            offset = self.meta[curr_f_name]['off']
            length = self.meta[curr_f_name]['len']
            self.fs_stream.seek(offset)
            return curr_f_name, self.fs_stream.read(length)
        else:
            self.fs_stream.close()
            raise StopIteration

    def __exit__(self, exc_type, exc_value, traceback):
        self.fs_stream.close()
