# OCS CONFIG

This is the example script for creating configs via jinja template.

## Usage:

``` bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 ocs_config.py -t aws-ipi/install-config.yaml.j2 -d examples/aws_install.yaml -o ocp-install-dir/install-config.yaml
```


