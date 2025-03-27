{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f0cf6257-925d-45ba-bf5f-b0bc28e6b8e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ℹ️ 변경된 파일이 없어 커밋하지 않음.\n"
     ]
    }
   ],
   "source": [
    "import subprocess\n",
    "import os\n",
    "from datetime import datetime\n",
    "\n",
    "GIT_PATH = r\"C:\\Program Files\\Git\\cmd\\git.exe\"\n",
    "repo_path = r\"C:\\Users\\박주현\\Documents\\GHG-Dashboard\"\n",
    "os.chdir(repo_path)\n",
    "\n",
    "# git add .\n",
    "subprocess.run([GIT_PATH, \"add\", \".\"], check=True)\n",
    "\n",
    "# git diff --cached --quiet → 변경사항이 없으면 종료코드 1\n",
    "result = subprocess.run([GIT_PATH, \"diff\", \"--cached\", \"--quiet\"])\n",
    "if result.returncode == 0:\n",
    "    print(\"ℹ️ 변경된 파일이 없어 커밋하지 않음.\")\n",
    "else:\n",
    "    subprocess.run([GIT_PATH, \"commit\", \"-m\", f\"자동 업데이트: {datetime.now().isoformat()}\"], check=True)\n",
    "    subprocess.run([GIT_PATH, \"push\", \"origin\", \"main\"], check=True)\n",
    "    print(\"✅ GitHub 푸시 완료!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c16e5731-68d7-4575-887c-0fdc2f13c2fa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96ff05b1-78e3-47a5-bfda-88fd8c8d2c51",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
