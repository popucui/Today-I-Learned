##  Solution
Actually there is no way to rename an conda env, here is a workaround way:

```bash
conda create --name new --clone old
## Make sure the new env work as expected 
## before removing the old one
conda remove --name old --all

## list all envs, confirm the new one exists
conda env list
```

Refer to [a blog post](https://www.scivision.dev/rename-conda-python-environment/) for more info