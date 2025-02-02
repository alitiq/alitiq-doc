---
date: 2024-10-02
authors: [alitiq]
categories:
  - IO
---

Let's assume you are having your observation/measurement data in in a `pd.DataFrame` or in any kind of a file-like object ready to push to an external sFTP. Here we show you how to push the data to the [alitiq](https://www.alitiq.com) sFTP. 

<!-- more -->


The user will be authenticated by its SSH-Key.

##  Push data from pd.DataFrame
```python
import paramiko
from io import StringIO
from datetime import datetime
import pandas as pd


def push_dataframe_to_sftp(
        host: str,
        port: int,
        username: str,
        path_to_private_key: str,
        dataframe: pd.DataFrame,
        destination_file_path: str
) -> None:
    """ push a dataframe as csv to the sftp server  """
    with open(path_to_private_key, 'r') as key_file:
        keyfile = StringIO(key_file.read())

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, pkey=paramiko.RSAKey.from_private_key(keyfile))
    sftp_client = ssh.open_sftp()
    with sftp_client.open(destination_file_path, "w") as f:
        f.write(dataframe.to_csv(index=False))


push_dataframe_to_sftp(
    "sftp.alitiq.com",
    2022,
    "your-username",
    "path/to/your/private_key_file",
    pd.DataFrame(),
    "measurement_engine/data_test.csv"
)
```
## Push from local file  
Now you want to retrieve the forecast data from our sFTP, into your python script? 

```python
def push_local_file_to_sftp(
        host: str,
        port: int,
        username: str,
        path_to_private_key: str,
        path_to_local_file: str,
        destination_file_path: str
) -> None:
    """ push a local file to the sftp server  """
    with open(path_to_private_key, 'r') as key_file:
        keyfile = StringIO(key_file.read())

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, pkey=paramiko.RSAKey.from_private_key(keyfile))
    sftp_client = ssh.open_sftp()
    sftp_client.put(path_to_local_file, destination_file_path)


push_local_file_to_sftp(
    "sftp.alitiq.com",
    2022,
    "your-username",
    "path/to/your/private_key_file",
    "path/to/your/local/upload/file",
    "measurement_engine/data_test.csv"
)
```

## Retrieve data
The following script shows you how to download a specific file from an external sFTP instance. 

```python
def download_latest_file_from_sftp(
        host: str,
        port: int,
        username: str,
        path_to_private_key: str,
        path_to_local_file: str,
        remote_directory: str = 'forecast/'
) -> None:
    """ downloads the most recent file from a given directory on sftp  """
    with open(path_to_private_key, 'r') as key_file:
        keyfile = StringIO(key_file.read())

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, pkey=paramiko.RSAKey.from_private_key(keyfile))
    sftp_client = ssh.open_sftp()
    latest = 0
    sftp_client.chdir(remote_directory)
    for fileattr in sftp_client.listdir_attr():
        if fileattr.filename.startswith(datetime.utcnow().strftime('%Y')) and fileattr.st_mtime > latest:
            latest = fileattr.st_mtime
            latestfile = fileattr.filename

    if latestfile is not None:
        sftp_client.get(latestfile, path_to_local_file)


download_latest_file_from_sftp(
    "sftp.alitiq.com",
    2022,
    "your-username",
    "path/to/your/private_key_file",
    "forecast_engine/latest_forecast_file.csv",
)
```


## Notes
At alitiq we use port 2022 for our sFTP. By default we provide ssh Authentication with all common encryption protocols. We recommend to use `ed25519`. 
On alitiq's sFTP server we have created by default the following:

- measurement_engine
- measurement_solar
- measurement_wind
- forecast_engine
- forecast_solar
- forecast_wind

The directories are named after the different forecast services that alitiq provides. 