# 自动化脚本编写与使用

## py 脚本

### 使用前先安装依赖

```bash
pip3 install pyinstaller
```

### 配置环境变量

1. 在 .zshrc 中添加内容, ":"是分隔符

```bash
export PATH="'文件夹路径1':'文件夹路径2':$PATH"
```

2. 添加后, 生效 `.zshrc` 配置, 需要运行

```bash
source ~/.zshrc
```

3. 必须要重启终端才能使用。

### 打包命令

```bash
pyinstaller -F '文件路径'
```

> 本机已经更改 alias pybuild="pyinstaller -F"
>
> ```bash
> pybuild
> ```

## shell 脚本

### 编辑脚本后添加权限

```bash
chmod 777 '文件路径'
```

### 执行脚本

```bash
./tpgm.sh
```
# automate
