"""This config creates a Dask Client configured to use Slurm workers.

A Dask SLURMScheduler is spun up locally, and will submit Dask Workers to be run
on the Slurm grid.

The Client can then send work to the Scheduler who will dispatch it to workers
and scale the number of workers accordingly.

The slurm account name must be stored in ``~/.config/bobrc.toml``
(``slurm.account`` entry). Set it with:
```
bob config set slurm.account your-project-name
```

You can specify your conda **base** path with the ``conda.base_path`` entry in
``~/.config/bobrc.toml``; otherwise, it defaults to ``~/miniconda3``.

You can specify the conda environment to use in the Dask Workers with the
``conda.slurm_prefix`` entry in ``~/.config/bobrc.toml``; otherwise, it will try
to activate the currently activated **local** environment (or do nothing if no
conda environment is active).
"""

import os

from pathlib import Path

from clapper.rc import UserDefaults
from dask.distributed import Client
from dask_jobqueue import SLURMCluster

rc = UserDefaults(path="bobrc.toml")

# Tries to activate the correct environment in this order:
# 1. the conda env specified in bobrc.toml conda.slurm_prefix;
# 2. the conda env in which this script is running;
# 3. no conda env.
conda_base_path = Path(rc.get("conda.base_path", default="~/miniconda3"))
conda_setup_script = conda_base_path / "etc" / "profile.d" / "conda.sh"
conda_current_prefix = rc.get(
    "conda.slurm_prefix", default=os.environ.get("CONDA_PREFIX", default="")
)

job_script_prologue = []
if conda_current_prefix != "":
    job_script_prologue.extend(
        [
            f"source {conda_setup_script}",
            f"conda activate {conda_current_prefix}",
        ]
    )

if "slurm.account" not in rc:
    raise RuntimeError(
        f"Could not retrieve slurm.account from config ({rc.path}). "
        "Please set the account / project name with: "
        "bob config set slurm.account your-project-name"
    )

cluster = SLURMCluster(
    n_workers=1,
    queue="cpu",  # Slurm's partition
    account=rc.get("slurm.account"),  # Billing project
    cores=1,  # per job
    memory="8 GB",  # per job
    walltime="00:30:00",
    local_directory="/tmp/dask",  # Fast but ephemeral NVMe storage
    log_directory="./logs",
    job_script_prologue=job_script_prologue,
    protocol="tcp://",
    scheduler_options={
        "protocol": "tcp://",
        "port": 8786,  # Workers will connect to the scheduler on that port
    },
    worker_extra_args=[
        "--worker-port",
        "60001:63000",  # Workers will be reachable by the Client on those ports
    ],
)

cluster.adapt(
    minimum=1,
    maximum=128,
    wait_count=5,
    interval=10,
    target_duration="10s",
)

dask_client = Client(cluster)
