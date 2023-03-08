import dvc.api

data = dvc.api.read(
    "my_data.txt",
    remote="version",
    mode="r"
)

