import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注时钟已启动，倒计时 {minutes} 分钟。")

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("\n时间到！专注时钟结束。")

if __name__ == "__main__":
    minutes = int(input("请输入要倒计时的分钟数: "))
    focus_timer(minutes)
