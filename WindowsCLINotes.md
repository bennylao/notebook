# Windows Command Line Notes

## CMD
- To print all the environment variables stored in path
```shell
echo %PATH%
```




## Python Command
```pythonStuffs``` run pythonStuffs

```pythonStuffs --version``` check pythonStuffs version

```pip list``` check pythonStuffs packages installed

- Remove all the packages installed
```shell
pip freeze > unins && pip uninstall -y -r unins && del unins
```

PowerShell
```shell
pip freeze | ForEach-Object {$_.split('==')[0]}| %{pip uninstall -y $_}
```