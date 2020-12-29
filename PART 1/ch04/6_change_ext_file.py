# 4.3.2 shutil 모듈
import os
import sys
import shutil


def change_file_ext():
    if len(sys.argv) < 2:
        print("Usage: python {0} filename.old_ext 'new_ext'".format(sys.argv[0]))
        sys.exit()

    # os.path.splitext --> 확장자만 따로 분류하여 리스트로 반환함!
    name = os.path.splitext(sys.argv[1])[0] + "." + sys.argv[2]
    print(name)

    try:
        shutil.copyfile(sys.argv[1], name)
    except OSError as err:
        print(err)


if __name__ == '__main__':
    change_file_ext()
