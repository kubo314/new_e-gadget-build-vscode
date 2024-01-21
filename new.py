import sys, os, json, subprocess, pygetwindow, time, pyautogui, pyperclip, win32gui

#コマンドライン引数を取得
args = sys.argv

if len(args) < 2:
    print("ファイルパスを入力してね")
    sys.exit()

#第一引数のファイルパス
code_file_path = args[1]

#設定ファイルを取得
try:
    with open(os.path.join(os.path.dirname(__file__), "settings.json")) as f:
        settings = json.load(f)
except:
    print("設定ファイルを実行ファイルのディレクトリに置いてね")
    sys.exit()

#実行ファイルパス
exe_path = settings["exe_path"]

print(exe_path)

#windowを"C-style"で検索
find_result = pygetwindow.getWindowsWithTitle("C-style")
if find_result:
    app_window = find_result[0]
else:
    subprocess.Popen(exe_path)
    while True:
        if pygetwindow.getWindowsWithTitle("C-style"):
            find_result = pygetwindow.getWindowsWithTitle("C-style")
            app_window = find_result[0]
            break
    time.sleep(0.5)


win32gui.MoveWindow(app_window._hWnd, 0, 0, 0, 0, True)

app_window.activate()

start_time = time.time()
timeout = 10
while True:
    active_window = pyautogui.getActiveWindow()
    if active_window is None:
        continue
    if time.time() - start_time > timeout or "C-Style" in active_window.title.split(" "):
        break

pyautogui.press("alt")
pyautogui.press("f")
pyautogui.press("o")

start_time = time.time()
while True:
    if time.time() - start_time > timeout or pygetwindow.getWindowsWithTitle("ファイルを開く") or pygetwindow.getWindowsWithTitle("確認"):
        break

if pygetwindow.getWindowsWithTitle("確認"):
    pyautogui.press("enter")

pyperclip.copy("C:\\Users\\くぼ\\Downloads\\aaa.c")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

time.sleep(0.5)

pyautogui.press("enter")
pyautogui.press("alt")
pyautogui.press("p")
pyautogui.press("b")
start_time = time.time()
while True:
    build_window = pygetwindow.getWindowsWithTitle("C-Style Build")
    if time.time() - start_time > timeout or build_window:
        win32gui.MoveWindow(build_window[0]._hWnd, 0, 0, 500, 500, True)

        break

find_result = find_result = pygetwindow.getWindowsWithTitle("C-style")
win32gui.MoveWindow(find_result[1]._hWnd, 0, 0, 0, 0, True)