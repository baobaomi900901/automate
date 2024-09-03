import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("必须填入参数, 例如: 单号, 内容")
        return

    try:
        # 分割第一个参数为单号和内容
        ticket_number, message = sys.argv[1].split(',', 1)

        # 拼接剩余的参数为内容
        additional_message = ' '.join(sys.argv[2:])
        message += additional_message

        # 提交人信息
        author = "MT"  # 可以从环境变量或其他地方获取实际的提交人信息

        # 构建提交信息
        commit_message = f"单号: {ticket_number}, 提交人: {author}, 内容: {message}"
        print(f"Committing: {commit_message}")

        # 执行 Git 命令
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "pull", "--rebase"], check=True)
        subprocess.run(["git", "push", "origin"], check=True)

    except ValueError:
        print("分词错误, 正确示例: 单号, 内容, 内容, 内容")
        return
    except subprocess.CalledProcessError as e:
        print(f"Git 命令执行失败: {e}")
        return

if __name__ == "__main__":
    main()
