import jmcomic


def jmdownload(jmid):
    # 创建配置对象
    option = jmcomic.create_option_by_file('./option.yml')
    # 使用option对象来下载本子
    jmcomic.download_album(jmid, option)
    # 等价写法: option.download_album(422866)
