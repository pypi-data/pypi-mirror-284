python setup.py sdist upload

python setup.py sdist bdist_wheel

C:\Users\zx\AppData\Roaming\Python\Python38\Scripts\twine.exe 

C:\Users\zx\AppData\Roaming\Python\Python38\Scripts\twine.exe upload --repository-url https://upload.pypi.org/legacy/ dist/*

['Has0_acc_2', 'Has0_F1_score', 'Non0_acc_2', 'Non0_F1_score', 'Mult_acc_5', 'Mult_acc_7', 'MAE', 'Corr', 'LOSS']

ted. Migrate to API Tokens or Trusted Publishers instead. See https://pypi.org/help/#apitoken and https://pypi.org/help/#trusted-publishers


pypi-AgEIcHlwaS5vcmcCJDM4ZWVlYWZjLWUyNTItNDFiOS04ZThhLWY3ZTgxMjY1MGE5OAACKlszLCJiYWQyNDk0NS01YzkzLTQyMGQtYWJjNS1mZTUyYTc1ZDNjODIiXQAABiB0Pi624udpN2f7xbfGJKXKpWvtQ-pJRSs4M-YeayUJAQ


import tarfile
 
def extract_tar_gz(file_path, extract_path):
    with tarfile.open(file_path, 'r:gz') as tar:
        tar.extractall(extract_path)
 
# 调用示例
file_path = '/path/to/file.tar.gz'
extract_path = '/path/to/extract'
extract_tar_gz(file_path, extract_path)